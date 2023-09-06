# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from collective.relationhelpers import api

class Donors(ViewletBase):

    def donors(self):
        return api.relations(self.context,
                             attribute="funding_partners")

    def index(self):
        return super(Donors, self).render()
