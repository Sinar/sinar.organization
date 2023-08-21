# -*- coding: utf-8 -*-

from collective import dexteritytextindexer
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
    Organizational Partner Roles following IATA Organizationl Role
    Codelist https://iatistandard.org/en/iati-standard/203/codelists/organisationrole/
    """

    # accountable partners
    dexteritytextindexer.searchable('accountable_partners')
    directives.widget('accountable_partners',
                      RelatedItemsFieldWidget,
                      pattern_options={
                          'basePath': '/',
                          'mode': 'auto',
                          'favourites': [],
                      }
                      )

    accountable_partners = RelationList(
        title=u'Accountable',
        description=u'''Organizations that are responsible for oversight
                        of the activity and it's outcomes''',
        required=False,
        value_type=RelationChoice(
            source=CatalogSource(portal_type='Organization'),
        ),
    )

    # beneficiary_partners
    dexteritytextindexer.searchable('beneficiary_partners')
    directives.widget('beneficiary_partners',
                      RelatedItemsFieldWidget,
                      pattern_options={
                          'basePath': '/',
                          'mode': 'auto',
                          'favourites': [],
                      }
                      )

    beneficiary_partners = RelationList(
        title=u'Beneficiaries',
        description=u'''Organizations that are beneficiares of the
                        activity or project''',
        required=False,
        value_type=RelationChoice(
            source=CatalogSource(portal_type='Organization'),
        ),
    )

    # Extending
    dexteritytextindexer.searchable('extending_partners')
    directives.widget('extending_partners',
                      RelatedItemsFieldWidget,
                      pattern_options={
                          'basePath': '/',
                          'mode': 'auto',
                          'favourites': [],
                      }
                      )

    extending_partners = RelationList(
        title=u'Extending',
        description=u'''Organizations that manages the budget and
                        direction of an activity or project on behalf of
                        the funding organization''',
        required=False,
        value_type=RelationChoice(
            source=CatalogSource(portal_type='Organization'),
        ),
    )

# Funding
    dexteritytextindexer.searchable('funding_partners')
    directives.widget('funding_partners',
                      RelatedItemsFieldWidget,
                      pattern_options={
                          'basePath': '/',
                          'mode': 'auto',
                          'favourites': [],
                      }
                      )

    funding_partners = RelationList(
        title=u'Funding',
        description=u'''Organizations which provides funds to the
                        activity or project''',
        required=False,
        value_type=RelationChoice(
            source=CatalogSource(portal_type='Organization'),
        ),
    )

    # implementing partners
    dexteritytextindexer.searchable('implementing_partners')
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
            'accountable_partners',
            'beneficiary_partners',
            'extending_partners',
            'funding_partners',
            'implementing_partners',
        ],
    )


@implementer(IPartners)
@adapter(IPartnersMarker)
class Partners(object):
    def __init__(self, context):
        self.context = context

    @property
    def accountable_partners(self):
        if safe_hasattr(self.context, 'accountable_partners'):
            return self.context.accountable_partners
        return None

    @accountable_partners.setter
    def accountable_partners(self, value):
        self.context.accountable_partners = value

    @property
    def beneficiary_partners(self):
        if safe_hasattr(self.context, 'beneficiary_partners'):
            return self.context.beneficiary_partners
        return None

    @beneficiary_partners.setter
    def beneficiary_partners(self, value):
        self.context.beneficiary_partners = value

    @property
    def extending_partners(self):
        if safe_hasattr(self.context, 'extending_partners'):
            return self.context.extending_partners
        return None

    @extending_partners.setter
    def extending_partners(self, value):
        self.context.extending_partners = value

    @property
    def funding_partners(self):
        if safe_hasattr(self.context, 'funding_partners'):
            return self.context.funding_partners
        return None

    @funding_partners.setter
    def funding_partners(self, value):
        self.context.funding_partners = value

    @property
    def implementing_partners(self):
        if safe_hasattr(self.context, 'implementing_partners'):
            return self.context.implementing_partners
        return None

    @implementing_partners.setter
    def implementing_partners(self, value):
        self.context.implementing_partners = value
