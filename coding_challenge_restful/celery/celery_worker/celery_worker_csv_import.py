import csv
from coding_challenge_restful.celery.celery_app import celery_app
from coding_challenge_restful.celery.celery_base import CeleryBaseTask
from coding_challenge_restful.celery.celery_base import task_initializer
from coding_challenge_restful.core.s3 import get_file_from_s3
from coding_challenge_restful.extensions import BulkCSVUpload, ProductStatus
from coding_challenge_restful.model_methods.product_methods import ProductMethods


@celery_app.task(bind=True, base=CeleryBaseTask, name="task_csv_import")
@task_initializer
def task_csv_import(self, *args, **kwargs):
    """Background task that runs a long function"""
    file_id = self.async_task_obj.payload.get('id')
    csv_object = self.db.query(BulkCSVUpload).filter(BulkCSVUpload.id == file_id).first()
    file_key = csv_object.csv.file_id
    bucket_name = "fulfilio-files"
    obj = get_file_from_s3(bucket_name, file_key)
    products_csv_object_encoded = obj['Body'].read()
    products_csv_object = products_csv_object_encoded.decode('utf-8')
    reader = csv.DictReader(
        products_csv_object.splitlines(),
        delimiter=','
    )

    reader.fieldnames = [header.strip().lower() for header in reader.fieldnames]

    cnt = 0
    for product in reader:
        cnt += 1
        if not product.get('sku'):
            continue
        sku = product.get('sku').lower()  # as sku is case-insensitive
        product_object = dict(
            name=product.get('name'),
            sku=sku,
            description=product.get('description'),
            status=ProductStatus.ACTIVE if cnt % 2 == 1 else ProductStatus.INACTIVE
        )

        record = ProductMethods.get_record_with_sku(self.db, sku)
        if not record:
            print("New record creation")
            try:
                pro_obj = ProductMethods.create_record(product_object)
                self.db.commit()
            except Exception as e:
                self.db.rollback()
                continue
        else:
            # update record or overwrite data
            print("Overwrite")
            updated_data = dict(
                name=product.get('name'),
                description=product.get('description'),
                status=ProductStatus.ACTIVE if cnt % 2 == 1 else ProductStatus.INACTIVE
            )
            ProductMethods.update_record(self.db, sku, updated_data)
            self.db.commit()
