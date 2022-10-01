from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
table_id = "ithome-bq-test.tv_shows.tv_shows_dashboard"

schema = [
    bigquery.SchemaField("ID", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("title", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("YEAR", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("AGE", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("NETFLIX", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("Hulu", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("Prime_video", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("Disney", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("Type", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("IMDb_score", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("IMDb_Total", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("RT_score", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("RT_Total", "INTEGER", mode="REQUIRED"),
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.

print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)