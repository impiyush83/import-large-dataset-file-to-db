from depot.manager import DepotManager
from flask import current_app as app, request, make_response, render_template, config, Config
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from coding_challenge_restful.core.filter_params_pagination import create_filter_params
from coding_challenge_restful.core.import_csv import send_csv_import_task
from coding_challenge_restful.extensions import db
from coding_challenge_restful.model_methods.bulk_csv_methods import BulkCSVUploadMethods
from coding_challenge_restful.model_methods.product_methods import ProductMethods
from coding_challenge_restful.utils.exceptions import exception_handle

config_name = 'coding_challenge_restful.settings.Config'
config = Config("")
config.from_object(config_name)


class Products(Resource):
    decorators = [exception_handle]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def post(self):
        """

    .. http:post::  /products

        This api will be used to send sku_data_import task to queue

        **Example request**:

        .. sourcecode:: http

           POST  /products  HTTP/1.1 HEADERS
           File

        **Example response**:

            {
                "message": "SUCCESS"
            }

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: success
        :statuscode 400: bad request error

        """
        products_file = request.files["products_csv"]
        products_file_object = products_file.read()
        if not DepotManager._default_depot:
            DepotManager.configure(
                'default',
                {
                    'depot.backend': 'depot.io.boto3.S3Storage',
                    'depot.access_key_id': config.get('AWS_ACCESS_KEY', None),
                    'depot.secret_access_key': config.get('AWS_SECRET_KEY', None),
                    'depot.bucket': 'fulfilio-files',
                    'depot.region_name': 'eu-central-1'
                }
            )
        csv_object = BulkCSVUploadMethods.create_record(dict(csv=products_file_object))
        db.commit()
        send_csv_import_task(csv_object.id)
        db.commit()
        return make_response(render_template('operations.html'), 200)

    def delete(self):
        """

    .. http:delete::  /products

        This api will be used to delete all products from the products tables

        **Example request**:

        .. sourcecode:: http

           DELETE  /products  HTTP/1.1

        **Example response**:

            {
                "message": "SUCCESS"
            }

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: success
        :statuscode 400: bad request error

        """
        ProductMethods.delete_all_records(db)
        db.commit()
        return make_response(render_template('operations.html'), 200)

    def get(self):
        """

    .. http:get::  /products

        This api will be used to filter and return products

        **Example request**:

        .. sourcecode:: http

           GET  /products?page="1"&name="name"&sku="sku"&description="desc"&status="active/inactive"  HTTP/1.1
           page is mandatory

        **Example response**:

            {
                "message": "SUCCESS"
            }

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: success
        :statuscode 400: bad request error

        """
        list_of_products = []
        params = request.args
        sku = params.get('sku')
        page = params.get('page')
        status = params.get("status")
        description = params.get("description")
        name = params.get('name')
        filter_params = dict()
        filter_params = create_filter_params(sku, description, name, status, filter_params)
        if not page:
            raise BadRequest("No page number")
        page = int(params.get('page'))
        all_products = ProductMethods.get_all_records_paginated(db, filter_params, page=page)
        for product in all_products:
            product_dict = dict(
                name=product.name,
                sku=product.sku,
                description=product.description,
                status=product.status.value
            )
            list_of_products.append(product_dict)
        return {"products": dict(page=page, items=list_of_products)}, 200
