from flask import current_app as app

from coding_challenge_restful.celery.celery_app import celery_app
from coding_challenge_restful.constants.common_constants import SUCCESS
from coding_challenge_restful.extensions import db
from coding_challenge_restful.model_methods.async_task_methods import AsyncTaskMethods


def send_task_to_queue(payload=None, task_name=None, queue_name=None, celery_application=celery_app):
    import pdb
    pdb.set_trace()
    record_obj = AsyncTaskMethods.create_record(payload)
    result = None
    message = SUCCESS
    try:
        result = celery_application.send_task(
            task_name,
            kwargs=dict(async_task_id=record_obj.id),
            queue=queue_name
        )
    except Exception as e:
        app.logger.error("celery send tasks failed with exc: {}".format(str(e)))
        message = str(e)
        print("Error in celery sending tasks to rabbitmq")
        AsyncTaskMethods.update_record_with_id(
            db,
            record_obj.id
        )
    else:
        AsyncTaskMethods.update_record_with_id(
            db,
            record_obj.id,
            task_id=result.id
        )
    return result, message
