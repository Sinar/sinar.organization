# -*- coding: utf-8 -*-

from plone import schema
from plone.app.z3cform.widget import SelectFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from sinar.organization import _
from zope.component import adapter
from zope.interface import implementer, Interface, provider


class IOrganizationTypeMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IOrganizationType(model.Schema):
    """
    """

    directives.widget(organization_type=SelectFieldWidget)
    organization_type = schema.Choice(
        title=_(u'Organization Type'),
        description=_(u'''
        Type that bests represents this organization.
        '''),

        required=False,
        vocabulary='sinar.organization.OrganizationType',
        ) 

@implementer(IOrganizationType)
@adapter(IOrganizationTypeMarker)
class OrganizationType(object):
    def __init__(self, context):
        self.context = context

    @property
    def organization_type(self):
        if safe_hasattr(self.context, 'organization_type'):
            return self.context.organization_type
        return None

    @organization_type.setter
    def organization_type(self, value):
        self.context.organization_type= value
