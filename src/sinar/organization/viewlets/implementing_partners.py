# -*- coding: utf-8 -*-

from collective.relationhelpers import api
from plone import api
from plone.app.layout.viewlets import ViewletBase


class ImplementingPartners(ViewletBase):

    def implementing(self):

        return api.relations(self.context,
                             attribute="implementing_partners")

    def index(self):
        return super(ImplementingPartners, self).render()
