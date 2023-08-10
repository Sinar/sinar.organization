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
from plone.autoform import directives
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.vocabularies.catalog import CatalogSource

class IPartnersMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IPartners(model.Schema):
    """
    """

    # beneficiaries

    directives.widget('beneficiaries',
                      RelatedItemsFieldWidget,
                      pattern_options={
                          'basePath': '/',
                          'mode': 'auto',
                          'favourites': [],
                      }
                      )

    beneficiaries = RelationList(
        title=u'Beneficiaries',
        description=u'''Organizations that are beneficiaries of an
                        activity or project''',
        required=False,
        value_type=RelationChoice(
            source=CatalogSource(portal_type='Organization'),
        ),
    )

    # donors
    directives.widget('donors',
                      RelatedItemsFieldWidget,
                      pattern_options={
                          'basePath': '/',
                          'mode': 'auto',
                          'favourites': [],
                      }
                      )

    donors = RelationList(
        title=u'Donors',
        description=u'''Organizations that are donors of an
                        activity or project''',
        required=False,
        value_type=RelationChoice(
            source=CatalogSource(portal_type='Organization'),
        ),
    )

    # implementing partners
    directives.widget('implementing_partners',
                      RelatedItemsFieldWidget,
                      pattern_options={
                          'basePath': '/',
                          'mode': 'auto',
                          'favourites': [],
                      }
                      )

    implementing_partners = RelationList(
        title=u'Implementing Partners',
        description=u'''Organizations that are implementing partners of an
                        activity or project''',
        required=False,
        value_type=RelationChoice(
            source=CatalogSource(portal_type='Organization'),
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
        self.context.donors = value

    @property
    def beneficiaries(self):
        if safe_hasattr(self.context, 'beneficiaries'):
            return self.context.beneficiaries
        return None

    @beneficiaries.setter
    def beneficiaries(self, value):
        self.context.beneficiaries = value

    @property
    def implementing_partners(self):
        if safe_hasattr(self.context, 'implementing_partners'):
            return self.context.implementing_partners
        return None

    @implementing_partners.setter
    def implementing_partners(self, value):
        self.context.implementing_partners = value
