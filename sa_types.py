from sqlalchemy import Integer
from sqlalchemy_utils import ChoiceType


# NOTE: Ensure you cause an import of the types here, since in the migration scripts,
# the types will be imported from this module

class EnumChoiceType(ChoiceType):
    def __repr__(self):
        return "{}()".format(Integer.__name__)
