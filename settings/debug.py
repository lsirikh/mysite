# base 파일의 내용을 모두 상속받음
from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

# WSGI application (base.py에서는 WSGI_APPLICATION 변수 삭제)
WSGI_APPLICATION = 'config.wsgi.debug.application'

# 디버그모드니까 DEBUG는 True
DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']