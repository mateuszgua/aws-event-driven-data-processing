import config
from get_json_data import get_api_get_random_users
from upload_file_s3 import upload_file

number_of_users = 5000

# response = get_api_get_random_users(number_of_users)
# print(response)
path_to_upload = './data/sample.json'
bucket_name = config.BUCKET_NAME
object_name = 'dummy_users_data.json'
response = upload_file(path_to_upload, bucket_name, object_name)
print(response)
