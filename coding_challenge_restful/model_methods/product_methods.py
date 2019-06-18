from coding_challenge_restful.basemodel import BaseModel
from coding_challenge_restful.extensions import Product, ProductStatus


class ProductMethods(BaseModel):
    model = Product

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

    @classmethod
    def get_all_records_paginated(cls, db, filters, page=1):
        limit = 25
        offset = (page - 1) * 25
        query = db.query(cls.model)
        for filter_param in filters:
            if filter_param == "sku":
                query = query.filter(cls.model.sku == filters[filter_param])
            elif filter_param == "name":
                query = query.filter(cls.model.name == filters[filter_param])
            elif filter_param == "description":
                query = query.filter(cls.model.description == filters[filter_param])
            else:
                if filters[filter_param] == "active":
                    query = query.filter(cls.model.status == ProductStatus.ACTIVE)
                else:
                    query = query.filter(cls.model.status == ProductStatus.INACTIVE)
        query = query.limit(limit)
        query = query.offset(offset)
        return query.all()
