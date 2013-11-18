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
#from plone import api

class QueryView(BrowserView):

    template = ViewPageTemplateFile('query_view.pt')

    
    def __call__(self):    
	context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
	
	all_jobs = catalog.searchResults(portal_type= 'SeniorProject.PloneAddOn.job', 
					 Creator = "user1")
	

	mt =  getToolByName(self, 'portal_membership') 
        currentUser = mt.getAuthenticatedMember() 
        currentUserGroup = currentUser.getGroups();
        print currentUserGroup
        print groups_tool.getGroupsByUserId('admin')
        
	retStringg = ""
	joblist=[]
	for brain in all_jobs:
	    joblist.append(brain)
            print brain['listCreators']
	
	self.all_jobs = getattr(self.context, 'all_jobss', joblist)
	return self.template()
    
    def do_status_compare(self):
	print 'aaaaaaaaaaaaaaaaaaa'
      
  
