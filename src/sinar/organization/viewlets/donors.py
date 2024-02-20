# -*- coding: utf-8 -*-

from collective.relationhelpers import api
from plone.app.layout.viewlets import ViewletBase


class Donors(ViewletBase):

    def donors(self):
        return api.relations(self.context,
                             attribute="funding_partners")

    def index(self):
        return super(Donors, self).render()
