from load_aws_credentials import load_aws_credentials
import boto3


def aws_api(credential_file, region):
    aws_key, aws_secret = load_aws_credentials(credential_file)

    session = boto3.session.Session(aws_access_key_id=aws_key, aws_secret_access_key=aws_secret,
                                    region_name=region)
    return session.resource('s3')
