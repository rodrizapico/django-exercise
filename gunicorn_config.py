import os

bind = '0.0.0.0:' + os.getenv('PORT', '8000')
reload = os.environ.get('DEBUG', default=0) != 'False'
