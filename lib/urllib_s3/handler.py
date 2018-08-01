# -*- coding: utf-8 -*-
from minio import Minio
from six.moves.urllib.error import URLError
from six.moves.urllib.request import BaseHandler, url2pathname

from .error import ServerNameError


class UrllibS3Handler(BaseHandler):
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
            minio_server = self.settings[server_name]
        except KeyError:
            raise ServerNameError('missing credential')

        minioClient = Minio(
            server_name,
            access_key=minio_server['access_key'],
            secret_key=minio_server['secret_key'],
            secure=minio_server['secure']
        )

        return minioClient.get_object(bucket_name, key_name)
