from .base import *

DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', 'www.mjcmauguiocarnon.com','mjcmauguiocarnon.com']

try:
    from .local import *
except ImportError:
    pass
