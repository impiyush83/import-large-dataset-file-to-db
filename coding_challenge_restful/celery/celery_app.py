from celery import Celery
from flask import Config

config_name = 'coding_challenge_restful.settings.Config'
config = Config("")
config.from_object(config_name)


CELERY_CONFIG = dict(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    enable_utc=True,
    broker_url=config.get('CLOUDAMQP_URL'),
    broker_pool_limit=1,  # Will decrease connection usage
    broker_heartbeat=None,  # We're using TCP keep-alive instead
    broker_connection_timeout=30,  # May require a long timeout due to Linux DNS timeouts etc
    result_backend=None,  # AMQP is not recommended as result backend as it creates thousands of queues
    event_queue_expires=60,  # Will delete all celeryev. queues without consumers after 1 minute.
    worker_prefetch_multiplier=1,  # Disable prefetching, it's causes problems and doesn't help performance
    worker_concurrency=50,
    # If you tasks are CPU bound, then limit to the number of cores, otherwise increase substainally
)

celery_app = Celery('task_csv_import', backend=config.get("CELERY_BACKEND"), broker=config.get('CLOUDAMQP_URL'))
celery_app.conf.update(**CELERY_CONFIG)
