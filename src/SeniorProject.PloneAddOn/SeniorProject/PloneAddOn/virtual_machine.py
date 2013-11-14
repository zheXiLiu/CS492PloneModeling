from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder


from SeniorProject.PloneAddOn import MessageFactory as _


# Interface class; used to define content-type schema.

class IVirtualMachine(form.Schema, IImageScaleTraversable):
    """
    AWS instance which will run a scientific model.
    """
    #form.model("models/virtual_machine.xml")
    accessKey = schema.TextLine(
            title=_(u"AWS Access Key"),
    )

    secretKey = schema.TextLine(
            title=_(u"AWS Secret Key"),
    )

    machineImage = schema.TextLine(
            title=_(u"Amazon Machine Image"),
    )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class VirtualMachine(Container):
    grok.implements(IVirtualMachine)
    
    def getTitle(self):
	return self.title

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# virtual_machine_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    """ sample view class """

    grok.context(IVirtualMachine)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
