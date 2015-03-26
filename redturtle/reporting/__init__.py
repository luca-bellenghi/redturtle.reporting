# -*- coding: utf-8 -*-

#from AccessControl import ModuleSecurityInfo
from Products.Archetypes import atapi
from Products.CMFCore import utils
from redturtle.reporting import config
from zope.i18nmessageid import MessageFactory

signupsheetMessageFactory = MessageFactory('redturtle.reporting')
pmf = MessageFactory('plone')

#ModuleSecurityInfo('collective.signupsheet').declarePublic('signupsheetMessageFactory')


def initialize(context):
    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(config.PROJECTNAME),
        config.PROJECTNAME)

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit('%s: %s' % (config.PROJECTNAME, atype.portal_type),
            content_types=(atype, ),
            permission=config.ADD_PERMISSIONS[atype.portal_type],
            extra_constructors=(constructor,),).initialize(context)
