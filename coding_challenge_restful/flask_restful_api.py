from flask_restful import Api
from coding_challenge_restful.urls import urls


def restful_api(app):

    api = Api(app, prefix='/')
    for url in urls:
        api.add_resource(
            url.resource,
            url.name,
            *url.endpoint,
            strict_slashes=False
        )
