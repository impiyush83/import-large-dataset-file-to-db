from flask import current_app as app, request
from flask_restful import Resource

from coding_challenge_restful.core.import_csv import send_csv_import_task
from coding_challenge_restful.utils.exceptions import exception_handle


class SKU(Resource):

    decorators = [exception_handle]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def post(self):
        """

    .. http:post::  /skus

        This api will be used to sku_data_import to queue

        **Example request**:

        .. sourcecode:: http

           POST  /skus  HTTP/1.1 HEADERS
           {
                "title": "delivery 1",
                "priority": "high/medium/low",
                "created_at": "datetime",
                "created_by": "1"
           }

        **Example response**:

            {
                "message": "SUCCESS"
            }

        .. sourcecode:: http

           HTTP/1.1 200 OK
           Vary: Accept


        :statuscode 200: responses homepage
        :statuscode 400: bad request error
        :statuscode 404: value error
        :statuscode 401: unauthorized

        """
        # returns a jwt token based on id
        data = request.json
        send_csv_import_task(data)
        return {"message": "SUCCESS"}, 200



