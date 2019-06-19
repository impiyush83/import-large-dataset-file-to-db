from boto3 import Session
from flask import Config

config_name = 'coding_challenge_restful.settings.Config'
config = Config("")
config.from_object(config_name)


def get_file_from_s3(bucket_name, file_key):
    boto_session = Session(
        aws_access_key_id=config.get('AWS_ACCESS_KEY', None),
        aws_secret_access_key=config.get('AWS_SECRET_KEY', None)
    )
    client = boto_session.client('s3')
    return client.get_object(Bucket=bucket_name, Key=file_key)
