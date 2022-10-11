# -*- coding: utf-8 -*-

# from sinar.organization import _
from plone.dexterity.browser.view import DefaultView
from zope.component import getUtility
from zope.interface import Interface
from zope.schema.interfaces import IVocabularyFactory


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class IOrganizationView(Interface):
    """ Marker Interface for IOrganizationView"""

class OrganizationView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('organization_view.pt')

    def organization_type_title(self):

        factory = getUtility(IVocabularyFactory,
                             'sinar.organization.OrganizationType')

        vocabulary = factory(self)
        if self.context.organization_type:
            term = vocabulary.getTerm(self.context.organization_type)
            return term.title
        else:
            return None



    def __call__(self):
        # Implement your own actions:
        return super(OrganizationView, self).__call__()
