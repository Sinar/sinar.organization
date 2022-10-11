# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets import ViewletBase
from plone.app.uuid.utils import uuidToObject


class ImplementingPartners(ViewletBase):

    def implementing(self):

        objects = []
        partners = self.context.implementing_partners
        for partner in partners:
            obj = uuidToObject(partner)
            objects.append(obj)

        return objects

    def index(self):
        return super(ImplementingPartners, self).render()
