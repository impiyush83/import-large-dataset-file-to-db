from depot.manager import DepotManager
from flask import current_app as app, request
from flask_restful import Resource

from coding_challenge_restful.constants.common_constants import SUCCESS
from coding_challenge_restful.core.import_csv import send_csv_import_task
from coding_challenge_restful.extensions import db
from coding_challenge_restful.model_methods.bulk_csv_methods import BulkCSVUploadMethods
from coding_challenge_restful.model_methods.product_methods import ProductMethods
from coding_challenge_restful.utils.exceptions import exception_handle


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
            DepotManager.configure('default', {'depot.storage_path': './files'})
        bulk_csv_object = BulkCSVUploadMethods.create_record(dict(csv=products_file_object))
        db.commit()
        send_csv_import_task(bulk_csv_object.id)
        db.commit()
        return {"message": SUCCESS}, 200

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
        return {"message": SUCCESS}, 200

    def get(self):
        """

    .. http:get::  /products

        This api will be used to filter and return products

        **Example request**:

        .. sourcecode:: http

           GET  /products  HTTP/1.1

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

        return {"message": SUCCESS}, 200
