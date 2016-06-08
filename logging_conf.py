# disable django logging
from django.db.backends import BaseDatabaseWrapper
from django.db.backends.util import CursorWrapper

if settings.DEBUG:
    BaseDatabaseWrapper.make_debug_cursor = lambda self, cursor: CursorWrapper(cursor, self)

# Disable requests logging
logging.getLogger("requests").setLevel(logging.WARNING)


date = t.localtime(t.time())
name = '%d_%d_%d.log' %(date[2],date[1],(date[0]%100))
path = 'logs/'       
filename = (path + name)
logging.basicConfig(filename= filename, level=logging.DEBUG, format='%(asctime)s %(message)s') 
