import uuid

from coding_challenge_restful.celery.celery_worker.worker_configuration import WorkerConfiguration
from coding_challenge_restful.celery.send_task import send_task_to_queue


def send_csv_import_task(file_id):
    """
    Function will send tasks to the csv_import_queue  queue with the
    customer payload

    :param file_id: String
    :return: None
    """

    payload = dict(payload=file_id, task_id=str(uuid.uuid1()))

    send_task_to_queue(
        payload=payload,
        task_name=WorkerConfiguration.import_csv_to_database.get('task_name'),
        queue_name=WorkerConfiguration.import_csv_to_database.get('queue_name'),
    )

