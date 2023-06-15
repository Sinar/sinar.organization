# -*- coding: utf-8 -*-

from plone.app.dexterity import textindexer
from plone import schema
from plone.app.textfield import RichText
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget, SelectFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from Products.CMFPlone.utils import safe_hasattr
from sinar.organization import _
from z3c.relationfield.schema import RelationChoice, RelationList
from zope.component import adapter
from zope.interface import implementer, Interface, provider


class IPartnersMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IPartners(model.Schema):
    """
    """

    # beneficiaries
    directives.widget(beneficiaries=SelectFieldWidget)
    beneficiaries = schema.List(
            title=u'Beneficiaries',
            description=u'''Organizations that are beneficiaries of an
            activity or project''',
            required=False,
            value_type=schema.Choice(
                vocabulary='sinar.organization.Organizations',
                ),
            )

    # donors
    directives.widget(donors=SelectFieldWidget)
    donors = schema.List(
            title=u'Donors',
            description=u'Organizations that have provided funding',
            required=False,
            value_type=schema.Choice(
                vocabulary='sinar.organization.Organizations',
                ),
            )

    # implementing partners
    directives.widget(implementing_partners=SelectFieldWidget)
    implementing_partners = schema.List(
            title=u'Implementing Partners',
            description=u'Partners implementing this item',
            required=False,
            value_type=schema.Choice(
                vocabulary='sinar.organization.Organizations',
                ),
            )


    # fieldset set the tabs on the edit form

    fieldset(
            'partners',
            label=_(u'Partners'),
            fields=[
                'donors',
                'implementing_partners',
                'beneficiaries',
                ],
            )

@implementer(IPartners)
@adapter(IPartnersMarker)
class Partners(object):
    def __init__(self, context):
        self.context = context

    @property
    def donors(self):
        if safe_hasattr(self.context, 'donors'):
            return self.context.donors
        return None

    @donors.setter
    def donors(self, value):
        self.context.donors= value

    @property
    def beneficiaries(self):
        if safe_hasattr(self.context, 'beneficiaries'):
            return self.context.beneficiaries
        return None

    @beneficiaries.setter
    def beneficiaries(self, value):
        self.context.beneficiaries= value

    @property
    def implementing_partners(self):
        if safe_hasattr(self.context, 'implementing_partners'):
            return self.context.implementing_partners
        return None

    @implementing_partners.setter
    def implementing_partners(self, value):
        self.context.implementing_partners= value
