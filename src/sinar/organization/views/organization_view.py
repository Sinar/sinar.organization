# -*- coding: utf-8 -*-

from plone.dexterity.browser.view import DefaultView
from sinar.organization import _


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class OrganizationView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('organization_view.pt')

    def __call__(self):
        # Implement your own actions:
        return super(OrganizationView, self).__call__()
