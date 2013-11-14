from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_parent, aq_inner
from zope.component import getMultiAdapter

from SeniorProject.PloneAddOn.job import IJob
import time
import ZODB.FileStorage
import ZODB.serialize
import operator

def time_compare(x, y):
    if x['start'] is None:
	return 1
    elif y['start'] is None:
	return -1
    elif x['start']<y['start']:
	return 1
    elif x['start']>y['start']:
	return -1
    else:
	return 0

def status_compare(x, y):
    if x['start'] is None:
	return -1
    elif y['start'] is None:
	return 1
    elif x['start']<y['start']:
	return -1
    elif x['start']>y['start']:
	return 1
    else:
	return 0

class JobsView(BrowserView):

    template = ViewPageTemplateFile('jobs_view.pt')


    def __call__(self):    
	context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
	
	all_jobs = catalog.searchResults(portal_type= 'SeniorProject.PloneAddOn.job')
	retStringg = ""
	joblist=[]
	for brain in all_jobs:
	    joblist.append(brain)
            print brain
	

	joblist.sort(time_compare)
	self.all_jobs = getattr(self.context, 'all_jobss', joblist)
	return self.template()
    
    def do_status_compare(self):
	#joblist.sort(status_compare)
        print 'aaaaaaaaaaaaaaaaaaa'
        #self.all_jobs = getattr(self.context, 'all_jobss', joblist)
  
