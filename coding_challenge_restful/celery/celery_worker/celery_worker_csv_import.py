from coding_challenge_restful.celery.celery_app import celery_app
from coding_challenge_restful.celery.celery_base import task_initializer
from coding_challenge_restful.celery.celery_base import CeleryBaseTask
from coding_challenge_restful.model_methods.product_methods import ProductMethods
from coding_challenge_restful.extensions import ProductStatus
import csv


@celery_app.task(bind=True, base=CeleryBaseTask, name="task_csv_import")
@task_initializer
def task_csv_import(self, *args, **kwargs):
    """Background task that runs a long function"""

    file_content = self.async_task_obj.payload.get('file_contents')
    reader = csv.DictReader(
        file_content.splitlines(),
        delimiter=','
    )

    reader.fieldnames = [header.strip().lower() for header in reader.fieldnames]

    for product in reader:
        product_object = dict(
            name=product.get('name'),
            sku=product.get('sku'),
            description=product.get('description'),
            status=ProductStatus.ACTIVE
        )
        pro_obj = ProductMethods.create_record(product_object)
    db.commit()
