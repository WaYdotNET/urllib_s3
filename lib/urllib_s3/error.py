# -*- coding: utf-8 -*-


class UrllibS3Error(Exception):
    """
    Base class for all exceptions

    :param message: User defined message.
    """

    def __init__(self, message, **kwargs):
        super(UrllibS3Error, self).__init__(**kwargs)
        self.message = message

    def __str__(self):
        return "{name}: message: {message}".format(
            name=self.__class__.__name__,
            message=self.message
        )


class ServerNameError(UrllibS3Error):
    """
    ServerNameError is raised when
    input endpoint s3 server not found in settings
    """
    pass
