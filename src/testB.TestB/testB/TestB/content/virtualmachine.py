"""Definition of the VirtualMachine content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from testB.TestB.interfaces import IVirtualMachine
from testB.TestB.config import PROJECTNAME

VirtualMachineSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

VirtualMachineSchema['title'].storage = atapi.AnnotationStorage()
VirtualMachineSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(VirtualMachineSchema, moveDiscussion=False)


class VirtualMachine(base.ATCTContent):
    """Content Type for virtualMachine"""
    implements(IVirtualMachine)

    meta_type = "VirtualMachine"
    schema = VirtualMachineSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(VirtualMachine, PROJECTNAME)
