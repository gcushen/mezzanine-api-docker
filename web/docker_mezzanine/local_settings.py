# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

# Disable debugging unless defined otherwise through environment variable.
DEBUG = True if os.getenv('DEBUG') == 'true' else False

WSGI_APPLICATION = 'docker_mezzanine.wsgi.application'

# Secret keys: make these unique, and don't share them with anybody.
SECRET_KEY = os.environ['SECRET_KEY']
NEVERCACHE_KEY = os.environ['NEVERCACHE_KEY']

# Docker PostgreSQL Database.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT']
    }
}
