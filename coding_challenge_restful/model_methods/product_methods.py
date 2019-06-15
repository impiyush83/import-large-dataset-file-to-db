from coding_challenge_restful.basemodel import BaseModel
from coding_challenge_restful.extensions import Product


class ProductMethods(BaseModel):
    model = Product

    @classmethod
    def get_all_sku_records(cls, db):
        record = db.query(cls).all()
        return record
