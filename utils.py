from coding_challenge_restful.constants.common_constants import CSV_HEADERS


def csv_header_validation(requested_file_obj):
    requested_file_obj.fieldnames = [header.strip().lower() for header in requested_file_obj.fieldnames]
    for header in CSV_HEADERS['BulkCSVProducts']:
        if header not in requested_file_obj.fieldnames:
            raise ValueError('Invalid Headers Found')
