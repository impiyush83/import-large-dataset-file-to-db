import datetime
from decimal import Decimal

import phonenumbers
from passlib.context import CryptContext
from phonenumbers import NumberParseException
from sqlalchemy_utils import PhoneNumber
from werkzeug.exceptions import BadRequest

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=10000
)

date_format = '%Y-%m-%d %H:%M:%S UTC'


def parse_date(date_str, _format=date_format):
    try:
        if date_str is None:
            return None
        date_time = datetime.strptime(date_str, _format)
    except ValueError:
        return None
    else:
        return date_time


def date_to_str(date):
    return date and date.strftime(date_format)


def parse_int(int_str):
    try:
        return int(int_str)
    except ValueError:
        return None
    except TypeError:
        return None


def parse_float(float_str):
    try:
        return float(float_str)
    except ValueError:
        return None
    except TypeError:
        return None
    except:
        return None


def parse_decimal(decimal_str):
    try:
        return Decimal(decimal_str)
    except ValueError:
        return None
    except TypeError:
        return None
    except:
        return None


def encrypt_password(password):
    return pwd_context.hash(password)


def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)


def parse_and_validate_phone_number_str(phone_number_str, phone_country_code):
    try:
        phone_number = parse_phone_number(phone_number_str, phone_country_code)
        if phone_number is None:
            return None
        return None if len(str(phone_number.national_number)) != 10 else phone_number
    except AttributeError:
        return None
    except TypeError:
        return None
    except IndexError:
        return None


def parse_phone_number(phone_number_str, phone_country_code):
    try:
        region_code = phonenumbers.region_code_for_country_code(int(phone_country_code))
        phone_number = PhoneNumber(phone_number_str, region_code)
        return phone_number
    except ValueError:
        return None
    except NumberParseException:
        return None


def check_geolocation(lat, lon):
    if float(-90) > float(lat):
        raise BadRequest("Invalid geolocation")
    if float(lat) > float(90):
        raise BadRequest("Invalid geolocation")
    if float(-180) > float(lon):
        raise BadRequest("Invalid geolocation")
    if float(lon) > float(180):
        raise BadRequest("Invalid geolocation")
