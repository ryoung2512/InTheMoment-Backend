from environs import Env
from pathlib import Path
import boto3
import requests 

env = Env()
env.read_env()

# AWS Settings
AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env.str("AWS_S3_REGION_NAME")
AWS_S3_ENDPOINT_URL = env.str("AWS_S3_ENDPOINT_URL")

S3DIRECT_DESTINATIONS = {
    'primary_destination': {
        'key': env.str("AWS_S3_FOLDER"),
        'allowed': ['image/jpg', 'image/jpeg', 'image/png', 'video/mp4'],
    },
}

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_S3_REGION_NAME
)

s3 = session.resource("s3")

bucket = s3.Bucket(name=AWS_STORAGE_BUCKET_NAME)

def upload_file_to_bucket(file_path, response):
    upload_response = requests.post(response['url'], data=response['fields'],
                         files={'file': open(file_path, 'rb')})

    return upload_response


def get_presigned_url_2(bucket, key):
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url(
            ClientMethod='put_object',
            Params={'Bucket': bucket, 'Key': key},
            ExpiresIn=1000
        )
    return url

def get_presigned_url(key):
    s3 = boto3.client('s3')
    bucket = "itmimages"
    
    return s3.generate_presigned_post(
        Bucket=bucket,
        Key=key,
        Fields={"acl": "public-read", "Content-Type": "image/jpeg"},
        Conditions=[
            {"acl": "public-read"},
            {"Content-Type": "image/jpeg"}
        ],
        ExpiresIn=3600
    )

def get_s3_client():
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_S3_REGION_NAME
    )
    return s3

