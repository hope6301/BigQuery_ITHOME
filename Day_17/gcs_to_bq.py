from google.cloud import bigquery
import glob
import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = glob.glob("*.json")[0]
# Construct a BigQuery client object.
# client = bigquery.Client()
# 2024/1/25 Implementation of new project='your-project-id' can be used normally
client = bigquery.Client(project='your-project-id')

# TODO(developer): Set table_id to the ID of the table to create.
table_id = "ithome-bq-test.tv_shows.tv_shows_dashboard"

job_config = bigquery.LoadJobConfig(
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
)

uri = "gs://ithome-bq-test/mysql_export/tv_shows_dashboard.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)
print("Loaded {} rows.".format(destination_table.num_rows))
