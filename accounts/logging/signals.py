import time as t
import logging
from accounts.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings 

# disable django logging
from django.db.backends import BaseDatabaseWrapper
from django.db.backends.util import CursorWrapper

if settings.DEBUG:
    BaseDatabaseWrapper.make_debug_cursor = lambda self, cursor: CursorWrapper(cursor, self)

'''
class InfoFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.INFO
  
'''


logger = logging.getLogger(__name__)
#logger.addFilter(InfoFilter())

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        email = instance.email
        logger.info('user_created=' + email) 
    else:
        email = instance.email
        logger.info('user_signedin=' + email)        
        
