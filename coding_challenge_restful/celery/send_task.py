from coding_challenge_restful.celery.celery_app import celery_app
from coding_challenge_restful.constants.common_constants import SUCCESS
from flask import current_app as app


def send_task_to_queue(payload=None, task_name=None, queue_name=None, celery_application=celery_app):
    result = None
    message = SUCCESS
    try:
        import pdb
        pdb.set_trace()
        result = celery_application.send_task(
            task_name,
            kwargs=dict(async_csv_data=payload),
            queue=queue_name
        )
        import pdb
        pdb.set_trace()
    except Exception as e:
        app.logger.error("celery send tasks failed with exc: {}".format(str(e)))
        message = str(e)
        print("Error in celery sending tasks to rabbitmq")
    else:
        pass
    return result, message
