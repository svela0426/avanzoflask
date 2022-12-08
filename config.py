
from distutils.command.config import config
from distutils.debug import DEBUG


class DevelopmentConfig():
    DEBUG=True

config={'development':DevelopmentConfig}