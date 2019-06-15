from functools import wraps
from flask import current_app as app
from werkzeug.exceptions import HTTPException
from flask_restful import abort

from coding_challenge_restful.extensions import db
from coding_challenge_restful.utils.custom_exceptions import RequestValidationException, NoResultFound, AuthenticationException, \
    ResourceAlreadyPresent, ConflictState


def exception_handle(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except RequestValidationException as val_err:
            app.logger.error(val_err)
            db.rollback()
            return abort(400, message=str(val_err))
        except NoResultFound as val_err:
            app.logger.error(val_err)
            db.rollback()
            return abort(400, message=str(val_err))
        except ValueError as val_err:
            app.logger.error(val_err)
            db.rollback()
            return abort(400, message=str(val_err))
        except AuthenticationException as e:
            app.logger.error(e)
            db.rollback()
            return abort(401, message=str(e))
        except HTTPException as e:
            app.logger.error(e)
            db.rollback()
            return abort(e.code, message=e.description)
        except KeyError as key_err:
            app.logger.error(key_err)
            db.rollback()
            return abort(400, message=str(key_err))
        except IOError as io_err:
            app.logger.error()
            db.rollback()
            return abort(403, message=str(io_err))
        except ResourceAlreadyPresent as e:
            app.logger.error(e)
            db.rollback()
            return abort(409, message=str(e))
        except ConflictState as e:
            app.logger.error(e)
            db.rollback()
            return abort(409, message=str(e))
        except Exception as e:
            app.logger.error(e)
            db.rollback()
            return abort(500, message=str(e))
    return wrapper