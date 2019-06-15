from coding_challenge_restful.celery.celery_app import celery_app
from coding_challenge_restful.constants.common_constants import SUCCESS


@celery_app.task(bind=True, name="task_csv_import")
def task_csv_import(self, *args, **kwargs):
    """Background task that runs a long function"""

    import pdb
    pdb.set_trace()
    return {"message": SUCCESS}

