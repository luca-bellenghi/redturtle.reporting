from Products.ATContentTypes.content.folder import ATFolder
from Products.Archetypes import atapi
from Products.PloneFormGen.content.form import (FormFolder, FormFolderSchema)
from plone import api
from redturtle.reporting.config import (logger, PROJECTNAME)
from redturtle.reporting.interfaces import (ITracker, ITrackerInitializer)
from zope.interface import implements


TrackerSchema = FormFolderSchema.copy() + atapi.Schema(())


class Tracker(FormFolder):
    """ Tracker class"""

    implements(ITracker)
    schema = TrackerSchema

    def initializeArchetype(self, **kwargs):
        """ Create initial Track configuration
        """
        ATFolder.initializeArchetype(self, **kwargs)
        portal_factory = api.portal.get_tool('portal_factory')
        if not api.user.is_anonymous() and not portal_factory.isTemporary(self):
            ITrackerInitializer(self).form_initializer(**kwargs)
        else:
            logger.debug("Anonymous user: not allowed to create fields")

atapi.registerATCT(Tracker, PROJECTNAME)
