# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets import ViewletBase
from collective.relationhelpers import api

class ImplementingPartners(ViewletBase):

    def implementing(self):

        return api.relations(self.context,
                             attribute="implementing_partners")

    def index(self):
        return super(ImplementingPartners, self).render()
