signup_schema = {
    'first_name': {'type': 'string', 'required': True},
    'last_name': {'type': 'string', 'required': True},
    'email_id': {'type': 'string', 'required': True},
    'mobile_number': {'type': 'string', 'required': True},
    'password': {'type': 'string', 'required': True},
    'source': {'type': 'string', 'required': True}
}


update_schema = {
    'first_name': {'type': 'string', 'required': False},
    'last_name': {'type': 'string', 'required': False},
    'email_id': {'type': 'string', 'required': False},
    'mobile_number': {'type': 'string', 'required': False},
    'password': {'type': 'string', 'required': False}
}
