from dagster import schedule
from jobs.online_store_data_ingestion import online_store_data_ingestion


# Schedule Jobs in CET TimeZone
@schedule(
    cron_schedule="*/2 * * * *",
    job=online_store_data_ingestion,
    execution_timezone="US/Central",
)
def online_store_data_ingestion_schedule(_context):
    return {}
