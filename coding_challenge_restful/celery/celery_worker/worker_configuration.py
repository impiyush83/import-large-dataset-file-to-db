
class WorkerConfiguration:
    import_csv_to_database = dict(
        task_name="task_csv_import",
        queue_name="csv_import_job_queue"
    )
