"""Definition of the Job content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from testA.TestA.interfaces import IJob
from testA.TestA.config import PROJECTNAME

JobSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

JobSchema['title'].storage = atapi.AnnotationStorage()
JobSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(JobSchema, moveDiscussion=False)


class Job(base.ATCTContent):
    """Description of the Example Type"""
    implements(IJob)

    meta_type = "Job"
    schema = JobSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Job, PROJECTNAME)
