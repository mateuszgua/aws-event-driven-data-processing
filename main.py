import app.config as config
from app.get_json_data import get_api_get_random_users
from app.upload_file_s3 import upload_file
from app.read_file_from_s3 import read_file
import time

number_of_users = 10
bucket_name = config.BUCKET_NAME

response = get_api_get_random_users(number_of_users)
print(response)
path_to_upload = './data/sample.json'
object_name = 'dummy_users_data.json'
response = upload_file(path_to_upload, bucket_name, object_name)
print(response)

file_name = 'personal_data.parquet'
time.sleep(10)
df = read_file(file_name, bucket_name)
print(df)
