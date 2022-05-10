# -*- coding: utf-8 -*-

# from sinar.organization import _
from plone.dexterity.browser.view import DefaultView
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IOrganizationView(Interface):
    """ Marker Interface for IOrganizationView"""


class OrganizationView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('organization_view.pt')

    def __call__(self):
        # Implement your own actions:
        return super(OrganizationView, self).__call__()
