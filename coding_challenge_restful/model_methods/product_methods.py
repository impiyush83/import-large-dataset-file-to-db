from coding_challenge_restful.basemodel import BaseModel
from coding_challenge_restful.extensions import Product


class ProductMethods(BaseModel):
    model = Product

    @classmethod
    def get_all_records(cls, db):
        return db.query(cls.model).all()

    @classmethod
    def delete_all_records(cls, db):
        db.query(cls.model).delete()
        db.flush()

    @classmethod
    def get_record_with_sku(cls, db, sku):
        return db.query(cls.model).filter(cls.model.sku == sku).first()

    @classmethod
    def update_record(cls, db, sku, updated_data):
        db.query(cls.model).filter(cls.model.sku == sku).update(updated_data)
        db.flush()
