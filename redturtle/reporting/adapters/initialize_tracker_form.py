# -*- coding: utf-8 -*-
from redturtle.reporting.interfaces import (ITrackerInitializer,
                                            ITracker)
from zope.component import adapts
from zope.interface import implements


class InitializeTrackerForm(object):
    adapts(ITracker)
    implements(ITrackerInitializer)

    def __init__(self, context):
        self.form = context

    def form_initializer(self, **kwargs):
        """
        The same as PloneformGen do, but we overrides to create objects we
        are interest on: name, surname, status, email
        """
