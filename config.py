import os
# Local Database URI commented out below
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:{}@localhost:5432/marvel'.format(os.environ.get('PGPASS'))
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgresql://wguemifjpyyqfg:24bc18386b5d3262dda45d2347ec577a070fb4f3fbf522dde490e6770ebc7a76@ec2-3-227-195-74.compute-1.amazonaws.com:5432/d73pd9ukavp8s7'
