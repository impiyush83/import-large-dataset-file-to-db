from functools import wraps

from cerberus import Validator as cerberus_validator
from flask import request

from coding_challenge_restful.utils.utils import parse_date, parse_int, parse_decimal


class Validator(cerberus_validator):

    def __init__(self, *args, **kwargs):
        if 'additional_context' in kwargs:
            self.additional_context = kwargs['additional_context']
        super(Validator, self).__init__(*args, **kwargs)

    def _validate_type_unicode(self, value):
        return True if type(value) is str else False

    def _validate_type_utc_date(self, value):
        date_value = parse_date(value)
        return True if date_value else False

    def _validate_type_integer_string(self, value):
        integer_value = parse_int(value)
        return True if integer_value is not None else False

    def _validate_type_decimal_string(self, value):
        decimal_value = parse_decimal(value)
        return True if decimal_value is not None else False


def schema_validator_restful(schema):
    def decorator(func):
        @wraps(func)
        def validate(*args, **kwargs):
            validator = Validator(schema)
            if validator.validate(request.json):
                return func(*args, **kwargs)
            else:
                return validator.errors, 400
        return validate
    return decorator
