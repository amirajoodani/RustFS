import boto3
from botocore.client import Config

client = boto3.client(
    "s3",
    endpoint_url="http://192.168.1.14:9000",
    aws_access_key_id="rustfsadmin",
    aws_secret_access_key="rustfsadmin",
    config=Config(signature_version="s3v4"),
    region_name="us-east-1"
)

bucket = "mybucket"

response = client.list_buckets()

for bucket in response["Buckets"]:
    print(bucket["Name"])

