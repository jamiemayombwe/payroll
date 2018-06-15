import dj_database_url
from decouple import config
from payroll.local_settings import *

DEBUG = False
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])


db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
