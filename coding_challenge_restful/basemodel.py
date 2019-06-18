from coding_challenge_restful.extensions import db


class BaseModel:
    model = None

    @classmethod
    def get_record_with_id(cls, model_id):
        return db.query(cls.model).filter(cls.model.id == model_id).first()

    @classmethod
    def create_record(cls, values):
        obj = cls.model(**values)
        db.add(obj)
        db.flush()
        return obj
