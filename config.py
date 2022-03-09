import os
# Local Database URI commented out below
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:{}@localhost:5432/marvel'.format(os.environ.get('PGPASS'))
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgresql://iytxcroajwyzzj:dff683d8f87b26d2aeb6f25781555662cd5017366cb7cf1354e6dfc302f8e6fc@ec2-184-73-198-174.compute-1.amazonaws.com:5432/delskuejia3n6c'
database_path = 'postgresql://postgres:{}@localhost:5432/marvel'.format(os.environ.get('PGPASS'))
AUTH0_DOMAIN='dev-r-0hid9s.us.auth0.com'
ALGORITHMS=['RS256']
API_AUDIENCE='Marvel'
CLIENT_ID='8J2ZSyjaw2JDKf5MFIzomNuBbGRKdEr7'
