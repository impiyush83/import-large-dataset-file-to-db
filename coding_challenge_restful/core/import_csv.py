from flask import current_app as app

from coding_challenge_restful.celery.send_task import send_task_to_queue


def send_csv_import_task(csv_import_task):
    """
    Function will send tasks to the csv_import_queue  queue with the
    customer payload

    :type csv_import_task: json_object
    :param csv_import_task: csv_import_task tasks details
    :return: None
    """

    app.logger.info(
        "inside send_delivery_task by user_id: {}".format(
            csv_import_task.created_by)
    )

    app.logger.info("payload for send_delivery_task: {}".format(csv_import_task))
    send_task_to_queue(
        payload=csv_import_task,
        task_name="csv_import",
        queue_name="csv_import_queue"
    )

