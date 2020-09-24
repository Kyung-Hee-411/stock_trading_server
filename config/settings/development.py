## 개발서버

from .import secret
from .base import *

SECRET_KEY = secret.SECRET_KEY
DEBUG = True
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'stock_trading',
        'USER': 'root',
        'PASSWORD': 'rudgmlgkrtjd',
        'HOST': 'stock-trading-postgredb.cinqw7ouyrxc.ap-northeast-2.rds.amazonaws.com',
        'PORT': 5432,
    }
}