
from distutils.command.config import config
from distutils.debug import DEBUG


class DevelopmentConfig():
    DEBUG=False

config={'development':DevelopmentConfig}