from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# check if it is deployed using docker or if is a development environment
USE_DOCKER = os.getenv('USE_DOCKER')

# development environment
if not USE_DOCKER:

	# SECURITY WARNING: keep the secret key used in production secret!
	SECRET_KEY = '&-aivg+u*-$w6vl@^i=1okl%jbh$wyj98n8jrndqve-gwm)6hm'

	# SECURITY WARNING: don't run with debug turned on in production!
	DEBUG = True
	ALLOWED_HOSTS = ['localhost', '127.0.0.1']
	TIME_ZONE = 'America/Sao_Paulo'
	LANGUAGE_CODE = 'en-us'

	# Django database setup
	DB_ENGINE = 'django.db.backends.sqlite3'
	DB_NAME = BASE_DIR / 'db.sqlite3'
	DB_USER = ''
	DB_PASSWORD = ''
	DB_HOST = ''
	DB_PORT = ''


# production environment [Docker]
else:
	# SECURITY WARNING: keep the secret key used in production secret!
	SECRET_KEY = '&-aivg+u*-$w6vl@^i=1okl%jbh$wyj98n8jrndqve-gwm)6hm'

	# SECURITY WARNING: don't run with debug turned on in production!
	DEBUG = os.getenv('DEBUG')
	ALLOWED_HOSTS = [os.getenv('ALLOWED_HOST')]
	TIME_ZONE = 'America/Sao_Paulo'
	LANGUAGE_CODE = 'en-us'

	# Django database setup
	DB_ENGINE = 'django.db.backends.postgresql_psycopg2'
	DB_NAME = os.getenv('DB_NAME')
	DB_USER = os.getenv('DB_USER')
	DB_PASSWORD = os.getenv('DB_PASSWORD')
	DB_HOST = os.getenv('DB_HOST')
	DB_PORT = ''