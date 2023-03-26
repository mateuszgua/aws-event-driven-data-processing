import boto3
import io
import pyarrow.parquet as pq


def read_file(s3_file_name, bucket):
    buffer = io.BytesIO()
    s3_resource = boto3.resource('s3')
    s3_object = s3_resource.Object(bucket, s3_file_name)
    s3_object.download_fileobj(buffer)
    table = pq.read_table(buffer)
    df = table.to_pandas()
    return df
