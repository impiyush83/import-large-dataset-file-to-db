#!/usr/bin/env bash
celery worker -A coding_challenge_restful.celery.celery_worker.celery_worker_csv_import -l info -c 1 -Ofair -Q csv_import_job_queue &