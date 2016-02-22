#from documents.models import Document
from django.conf import settings
import logging
import time as t
import logging
# disable django logging 
from django.db.backends import BaseDatabaseWrapper
from django.db.backends.util import CursorWrapper
import json

if settings.DEBUG:
    BaseDatabaseWrapper.make_debug_cursor = lambda self, cursor: CursorWrapper(cursor, self)
    
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

logger = logging.getLogger(__name__)
    

def log_annotation_created(request):
    annotation = json.loads(request.body)
    user = request.user.email
        

    if annotation['oa']['motivatedBy'] == 'oa:commenting':        
        comment_quote = annotation['quote']
        comment_content = annotation['oa']['hasBody']['chars']    
        documentID = annotation['uri']
        logger.info('comment_created=%s, user=%s, text=%s, documentID=%s' %(comment_content, user, comment_quote, documentID))
        pass
        # TODO
    elif annotation['oa']['motivatedBy'] == 'oa:highlighting':
        documentID = annotation['uri']
        highlight_content = annotation['quote']
        logger.info('highlight_created=__, user=%s, text=%s, documentID=%s'%(user, highlight_content, documentID))
        pass
        # TODO 
    elif annotation['oa']['motivatedBy'] == 'oa:classifying':
        documentID = annotation['uri']
        tag_label = annotation['neonion']['viewer']['conceptLabel']
        tag_content = annotation['oa']['hasBody']['label']        
        logger.info('tag_concept_created=%s, user=%s, Concept_label=%s_, motivation=oa:classifying_, documentID=%s'%(tag_content, user, tag_label, documentID))
        pass
        # TODO
    elif annotation['oa']['motivatedBy'] == 'oa:identifying':
        documentID = annotation['uri']
        tag_label = annotation['neonion']['viewer']['conceptLabel']
        tag_content = annotation['oa']['hasBody']['label'] 
        identificated_as = annotation['oa']['hasBody']['identifiedAs'] 
        logger.info('tag_concept_created=%s, user=%s, Concept_label=%s_, motivation=oa:identifying_, documentID=%s'%(tag_content, user, tag_label, documentID))
        pass
        # TODO 
    elif annotation['oa']['motivatedBy'] == 'oa:linking':
        documentID = annotation['uri']
        source = annotation['neonion']['viewer']['source']
        target = annotation['neonion']['viewer']['target']
        predicateLabel = annotation['neonion']['viewer']['predicateLabel']
        logger.info('link_created, predicateLabel=%s_, source=%s, target=%s, motivation=linking_, documentID=%s'%(predicateLabel, source, target, documentID))
        pass

        
def log_annotation_edited(request):
    annotation = json.loads(request.body)
    user = request.user.email
    if annotation['oa']['motivatedBy'] == 'oa:commenting': 
        documentID = annotation['uri']
        comment_quote = annotation['quote']
        comment_content = annotation['oa']['hasBody']['chars']        
        logger.info('comment_edited=%s, user=%s, text=%s, documentID=%s'%(comment_content, user, comment_quote, documentID))
        pass
        # TODO 
    elif annotation['oa']['motivatedBy'] == 'oa:classifying':
        documentID = annotation['uri']
        tag_label = annotation['neonion']['viewer']['conceptLabel']
        tag_content = annotation['oa']['hasBody']['label']       
        logger.info('tag_concept_edited=%s, user=%s, Concept_label=%s_, motivation=classifying_, documentID=%s'%(tag_content, user, tag_label, documentID))
        pass
        # TODO   
    elif annotation['oa']['motivatedBy'] == 'oa:identifying':
        documentID = annotation['uri']
        tag_label = annotation['neonion']['viewer']['conceptLabel']
        tag_content = annotation['oa']['hasBody']['label'] 
        identificated_as = annotation['oa']['hasBody']['identifiedAs']       
        logger.info('tag-concpt_edited=%s, user=%s, Concept_label=%s_, motivation=identifying_, documentID=%s'%(tag_content, user, tag_label, documentID))
        pass
        # TODO
    
       

            


def log_annotation_deleted(request):
    annotation = json.loads(request.body)
    user = request.user.email
    if annotation['oa']['motivatedBy'] == 'oa:commenting':
        documentID = annotation['uri']
        comment_quote = annotation['quote']
        comment_content = annotation['oa']['hasBody']['chars']       
        logger.info('comment_deleted=%s, user=%s, text: %s, documentID=%s'%(comment_content, user, comment_quote, documentID))
        pass
        # TODO
    elif annotation['oa']['motivatedBy'] == 'oa:highlighting':
        documentID = annotation['uri']
        highlight_content = annotation['quote']
        logger.info('highlight_deleted=__, user=%s, text=%s, documentID=%s'%(user, highlight_content, documentID))
        pass
        # TODO 
    elif annotation['oa']['motivatedBy'] == 'oa:classifying':
        documentID = annotation['uri']
        tag_label = annotation['neonion']['viewer']['conceptLabel']
        tag_content = annotation['oa']['hasBody']['label']       
        logger.info('tag_concept_deleted=%s, user=%s, Concept_label=%s_, motivation=oa:classifying_, documentID=%s'%(tag_content, user, tag_label, documentID))
        pass
        # TODO
    elif annotation['oa']['motivatedBy'] == 'oa:identifying':
        documentID = annotation['uri']
        tag_label = annotation['neonion']['viewer']['conceptLabel']
        tag_content = annotation['oa']['hasBody']['label'] 
        identificated_as = annotation['oa']['hasBody']['identifiedAs']       
        logger.info('tag_concept_deleted=%s, user=%s, Concept_label=%s_, motivation=oa:identifying_, documentID=%s'%(tag_content, user, tag_label, documentID))
        pass
        # TODO   
    elif annotation['oa']['motivatedBy'] == 'oa:linking':
        documentID = annotation['uri']
        source = annotation['neonion']['viewer']['source']
        target = annotation['neonion']['viewer']['target']
        predicateLabel = annotation['neonion']['viewer']['predicateLabel']
        logger.info('link_deleted, predicateLabel=%s_, source=%s, target=%s, motivation=linking_, documentID=%s'%(predicateLabel, source, target, documentID))
        pass
    
        
def info(request):
    body = request.body
    logger.info(body) 
    


#documentID = annotation['oa']['hasTarget']['hasSource']['@id']