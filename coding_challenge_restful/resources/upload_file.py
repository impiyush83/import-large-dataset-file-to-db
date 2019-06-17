from flask import current_app as app, make_response, render_template
from flask_restful import Resource

from coding_challenge_restful.utils.exceptions import exception_handle


class UploadFile(Resource):
    decorators = [exception_handle]

    def __init__(self):
        app.logger.info('In the constructor of {}'.format(self.__class__.__name__))

    def get(self):
        return make_response(render_template('upload_file.html'), 200)
