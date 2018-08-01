# -*- coding: utf-8 -*-
from six.moves.urllib.request import build_opener, install_opener
from .handler import UrllibS3Handler


def setup(settings):
    opener = build_opener(UrllibS3Handler(settings=settings))
    install_opener(opener)
