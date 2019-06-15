from coding_challenge_restful.celery.celery_app import celery_app
from coding_challenge_restful.celery.celery_base import task_initializer
from coding_challenge_restful.celery.celery_base import CeleryBaseTask


@celery_app.task(bind=True, base=CeleryBaseTask, name="task_csv_import")
@task_initializer
def task_csv_import(self, *args, **kwargs):
    """Background task that runs a long function"""

