from flask import current_app as app, request
from flask_restful import Resource

from coding_challenge_restful.core.import_csv import send_csv_import_task
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
        import pdb
        pdb.set_trace()
        products_file = request.files["products_csv"]
        products_file_object = products_file.read()
        products_file_object = products_file_object.decode('utf-8')
        send_csv_import_task(products_file_object)
        return {"message": "SUCCESS"}, 200



