import os
from functools import wraps

import celery
from depot.manager import DepotManager
from flask import Config

from coding_challenge_restful.extensions import db, AsyncTask, s3_client

config_name = 'coding_challenge_restful.settings.Config'
config = Config("")
config.from_object(config_name)


class CeleryBaseTask(celery.Task):

    def on_success(self, retval, task_id, args, kwargs):
        """Success handler.

        Run by the worker if the task executes successfully.

        Arguments:
            retval (Any): The return value of the task.
            task_id (str): Unique id of the executed task.
            args (Tuple): Original arguments for the executed task.
            kwargs (Dict): Original keyword arguments for the executed task.

        Returns:
            None: The return value of this handler is ignored.
        """
        print("Success")
        self.db.flush()
        self.db.commit()

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """Error handler.

        This is run by the worker when the task fails.

        Arguments:
            exc (Exception): The exception raised by the task.
            task_id (str): Unique id of the failed task.
            args (Tuple): Original arguments for the task that failed.
            kwargs (Dict): Original keyword arguments for the task that failed.
            einfo (~billiard.einfo.ExceptionInfo): Exception information.

        Returns:
            None: The return value of this handler is ignored.
        """
        print("Failure")
        self.db.rollback()

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        """Handler called after the task returns.

        Arguments:
            status (str): Current task state.
            retval (Any): Task return value/exception.
            task_id (str): Unique id of the task.
            args (Tuple): Original arguments for the task.
            kwargs (Dict): Original keyword arguments for the task.
            einfo (~billiard.einfo.ExceptionInfo): Exception information.

        Returns:
            None: The return value of this handler is ignored.
        """
        print("After return success")
        self.db.session.remove()


def task_initializer(fn):
    """Instantiate a logger at the decorated class instance level."""

    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        self.db = db
        async_task_obj = self.db.query(AsyncTask).filter(
            AsyncTask.id == kwargs.get("async_task_id")
        ).first()
        self.s3_client = s3_client
        self.async_task_obj = async_task_obj
        print(fn.__name__)
        if not DepotManager._default_depot:
            DepotManager.configure('default', {
                'depot.backend': 'depot.io.boto3.S3Storage',
                'depot.access_key_id': config.get('AWS_ACCESS_KEY', None),
                'depot.secret_access_key': config.get('AWS_SECRET_KEY', None),
                'depot.bucket': 'fulfilio-files',
                'depot.region_name': 'eu-central-1'
            }
                                   )
        return fn(self, *args, payload=async_task_obj.payload, **kwargs)

    return wrapper
