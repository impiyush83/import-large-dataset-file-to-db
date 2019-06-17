from coding_challenge_restful.basemodel import BaseModel
from coding_challenge_restful.extensions import AsyncTask


class AsyncTaskMethods(BaseModel):
    model = AsyncTask

    @staticmethod
    def update_record_with_id(db, async_task_id, **kwargs):
        db.query(AsyncTask).filter(AsyncTask.id == async_task_id).update(kwargs)
        db.flush()

    @staticmethod
    def get_record_with_payload(db, payload=None):
        obj = db.query(AsyncTask).filter(AsyncTask.payload == payload).first()
        return obj

    @staticmethod
    def get_record_with_id(db, job_id=None):
        obj = db.query(AsyncTask).filter(AsyncTask.id == job_id).first()
        return obj
