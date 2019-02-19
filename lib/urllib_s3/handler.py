# -*- coding: utf-8 -*-
import boto3
from botocore.client import Config
from six.moves.urllib.error import URLError
from six.moves.urllib.request import url2pathname, HTTPSHandler

from .error import ServerNameError


class UrllibS3Handler(HTTPSHandler):
    def __init__(self, settings):
        self.settings = settings
        super(UrllibS3Handler, self).__init__()

    def s3_open(self, req):
        server_name = req.host
        bucket_name = url2pathname(req.selector).split('/')[1]
        key_name = req.selector.replace("/{bucket_name}/".format(
            bucket_name=bucket_name), '')

        if not bucket_name or not key_name:
            raise URLError(
                'url must be in the format '
                's3://<server_name>/<bucket>/<object>'
            )
        try:
            credential = self.settings[server_name]
        except KeyError:
            raise ServerNameError('missing credential')

        s3 = boto3.client(
            's3',
            endpoint_url="https://{server}".format(server=server_name),
            aws_access_key_id=credential['access_key'],
            aws_secret_access_key=credential['secret_key'],
            config=Config(signature_version='s3v4'),
            region_name=credential.get('region_name', 'us-east-1')
        )
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={'Bucket': bucket_name, 'Key': key_name},
            ExpiresIn=3600
        )
        req.full_url = url
        return self.https_open(req)
