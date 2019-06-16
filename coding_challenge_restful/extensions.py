from enum import Enum
from depot.fields.sqlalchemy import UploadedFileField
import inflection
from flask.config import Config
from flask_migrate import Migrate
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_wrapper import SQLAlchemy

from sa_types import EnumChoiceType

config_name = 'coding_challenge_restful.settings.Config'
config = Config('')
config.from_object(config_name)

isolation_level = 'READ COMMITTED'
db = SQLAlchemy(
    uri=config['DATABASE_URL'],
    isolation_level=isolation_level
)
migrate = Migrate(compare_type=True)
# Create Models
Model = db.Model


# Models are defined here
class SurrogatePK(object):
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, autoincrement=True, primary_key=True)


class HasTablename(object):
    @declared_attr
    def __tablename__(cls):
        return inflection.underscore(cls.__name__)


class Base(HasTablename, SurrogatePK):
    def update_attributes(self, dict):
        for name, value in list(dict.items()):
            setattr(self, name, value)

    def __repr__(self):
        return '<{model}({id})>'.format(model=self.__class__.__name__, id=self.id)


class ProductStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class Product(Base, Model):
    name = Column(String(256), nullable=False)
    sku = Column(String(256), unique=True, nullable=False, index=True)
    description = Column(String(1024), nullable=False)
    status = Column(EnumChoiceType(ProductStatus, impl=String(128)), nullable=False, index=True)


class AsyncTaskStatus(Enum):
    PENDING = 'PENDING'
    IN_PROGRESS = 'IN_PROGRESS'
    WORKER_COMPLETE = 'WORKER_COMPLETE'
    EXCEPTION = 'EXCEPTION'
    DONE = 'DONE'


class AsyncTask(Base, Model):
    __tablename__ = 'async_task'

    task_id = Column(String(64), index=True)
    payload = Column(JSONB)
    task_status = Column(
        EnumChoiceType(AsyncTaskStatus, impl=String(64)),
        default=AsyncTaskStatus.PENDING,
        nullable=False, index=True
    )


class BulkCSVUpload(Base, Model):
    __tablename__ = 'bulk_csv_upload'

    csv = Column(UploadedFileField(), nullable=False)
