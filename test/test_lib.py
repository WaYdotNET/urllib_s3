# -*- coding: utf-8 -*-
import pytest
from six.moves.urllib.error import URLError
from six.moves.urllib.request import urlopen
from lib import urllib_s3
from lib.urllib_s3.error import ServerNameError



def test_call_unknown_protocol():
    with pytest.raises(URLError):
        urlopen('s3://fake/url.png')


def test_missing_setting():
    with pytest.raises(TypeError):
        urllib_s3.setup()


def test_urllib_s3_with_wrong_credential():
    urllib_s3.setup({})
    with pytest.raises(ServerNameError):
        urlopen('s3://fake/url.png')


def test_get_resource(mocker):
    d = {
        'fake': {
            'access_key': 'k',
            'secret_key': 'k',
            'secure': False,
        }
    }
    mocker.patch('botocore.signers.generate_presigned_url', return_value='https://none/url.png')
    mocker.patch('six.moves.urllib.request.HTTPSHandler.https_open', return_value='https://fake/presigned_url.png')
    urllib_s3.setup(d)
    assert urlopen('s3://fake/url.png') == 'https://fake/presigned_url.png'
