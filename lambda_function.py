import json
import boto3
from botocore.client import Config
import zipfile

def lambda_handler(event, context):

    s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

    build_bucket = s3.Bucket('portfoliobuild.keagan.cloud')
    portfolio_bucket = s3.Bucket('portfolio.keagan.cloud')

    # On Windows, this will need to be a different location than /tmp
    build_bucket.download_file('portfolioBuild.zip', '/tmp/portfolioBuild.zip')

    with zipfile.ZipFile('/tmp/portfolioBuild.zip') as myzip:
        for nm in myzip.namelist():
            obj = myzip.open(nm)
            portfolio_bucket.upload_fileobj(obj, nm)
            portfolio_bucket.Object(nm).Acl().put(ACL='public-read')    # TODO implement
    return'Hello from Lambda!'
