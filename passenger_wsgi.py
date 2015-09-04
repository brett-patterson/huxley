import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + '/huxley')

INTERP = os.path.join(os.getcwd(), 'env/bin/python')

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, os.path.join(os.getcwd(), 'env/bin'))
sys.path.insert(0, os.path.join(os.getcwd(), 'env/lib/python2.7/site-packages/django'))
sys.path.insert(0, os.path.join(os.getcwd(), 'env/lib/python2.7/site-packages'))

os.environ['DJANGO_SETTINGS_MODULE'] = "huxley.settings"

import django
django.setup()

from django.core.handlers.wsgi import WSGIHandler
from paste.exceptions.errormiddleware import ErrorMiddleware
application = ErrorMiddleware(WSGIHandler(), debug=True)
