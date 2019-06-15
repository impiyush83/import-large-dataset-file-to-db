from coding_challenge_restful.celery.send_task import send_task_to_queue


def send_csv_import_task(csv_import_task):
    """
    Function will send tasks to the csv_import_queue  queue with the
    customer payload

    :type csv_import_task: json_object
    :param csv_import_task: csv_import_task tasks details
    :return: None
    """

    send_task_to_queue(
        payload=csv_import_task,
        task_name="task_csv_import",
        queue_name="csv_import_job_queue"
    )

