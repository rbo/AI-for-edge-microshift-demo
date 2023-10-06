from os import environ


def _read_from_environment(variable1, variable2):
    value1 = environ.get(variable1)
    return_value = value1 if value1 else environ.get(variable2)
    return return_value


endpoint_url = _read_from_environment('S3_ENDPOINT', 'AWS_S3_ENDPOINT')
access_key = _read_from_environment('S3_ACCESS_KEY', 'AWS_ACCESS_KEY_ID')
secret_key = _read_from_environment('S3_SECRET_KEY', 'AWS_SECRET_ACCESS_KEY')
bucket_name = _read_from_environment('S3_BUCKET', 'AWS_S3_BUCKET')

print(f'S3 access key: {access_key[:5]}...')
print(f'S3 secret key: {secret_key[:5]}...')
print(f'S3 endpoint URL: {endpoint_url}')
print(f'S3 bucket name: {bucket_name}')
