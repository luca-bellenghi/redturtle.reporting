from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.base import registerATCT
from Products.Archetypes import atapi
from Products.DataGridField.DataGridField import DataGridField
from Products.DataGridField.DataGridWidget import DataGridWidget
from Products.PloneFormGen.content.form import (FormFolder, FormFolderSchema)
from plone import api
from redturtle.reporting import rrmf as _
from redturtle.reporting.config import (logger, PROJECTNAME)
from redturtle.reporting.interfaces import (ITracker, ITrackerInitializer)
from zope.interface import implements


TrackerSchema = FormFolderSchema.copy() + atapi.Schema((

    DataGridField(
        name='availableAreas',
        default=({'id': 'ui',
                  'title': 'User interface',
                  'description': 'User interface issues'},
                 {'id': 'functionality',
                  'title': 'Functionality',
                  'description': 'Issues with the basic functionality'},
                 {'id': 'process',
                  'title': 'Process',
                  'description':
                  'Issues relating to the development process itself'}),
        widget=DataGridWidget(
            label=_(u'Poi_label_availableAreas',
                    default=u"Areas"),
            description=_(
                u'Poi_help_availableAreas',
                default="Enter the issue topics/areas for this tracker."),
            column_names=('Short name', 'Title', 'Description'),
        ),
        allow_empty_rows=False,
        required=True,
        validators=('isDataGridFilled', ),
        columns=('id', 'title', 'description',)
    ),

    DataGridField(
        name='availableIssueTypes',
        default=({'id': 'bug',
                  'title': 'Bug',
                  'description': 'Functionality bugs in the software'},
                 {'id': 'feature',
                  'title': 'Feature',
                  'description': 'Suggested features'},
                 {'id': 'patch',
                  'title': 'Patch',
                  'description': 'Patches to the software'}),
        widget=DataGridWidget(
            label=_(u'Poi_label_availableIssueTypes',
                    default=u"Issue types"),
            description=_(u'Poi_help_availableIssueTypes',
                          default=u"Enter the issue types for this tracker."),
            column_names=('Short name', 'Title', 'Description',),
        ),
        allow_empty_rows=False,
        required=True,
        validators=('isDataGridFilled',),
        columns=('id', 'title', 'description')
    ),
    atapi.LinesField(
        name='availableSeverities',
        default=['Critical', 'Important', 'Medium', 'Low'],
        widget=atapi.LinesWidget(
            label=_(u'Poi_label_availableSeverities',
                    default=u"Available severities"),
            description=_(
                u'Poi_help_availableSeverities',
                default=(u"Enter the different type of issue severities "
                         u"that should be available, one per line.")),
        ),
        required=True
    ),

    atapi.StringField(
        name='defaultSeverity',
        default='Medium',
        widget=atapi.SelectionWidget(
            label=_(u'Poi_label_defaultSeverity',
                    default=u"Default severity"),
            description=_(
                u'Poi_help_defaultSeverity',
                default=u"Select the default severity for new issues."),
        ),
        enforceVocabulary=True,
        vocabulary='getAvailableSeverities',
        required=True
    ),
    atapi.IntegerField(
        name='daysBeforeDeadline',
        default=15,
        widget=atapi.IntegerWidget(
            label=_(u'days_before_deadline'),
            description=_(u'days_before_deadline'),
        ),
    ),
    atapi.IntegerField(
        name='reminderBeforeDeadline',
        default=2,
        widget=atapi.IntegerWidget(
            label=_(u'reminder_before_deadline'),
            description=_(u'reminder_before_deadline'),
        )
    )
))


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

registerATCT(Tracker, PROJECTNAME)
