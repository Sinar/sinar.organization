# -*- coding: utf-8 -*-

from collective import dexteritytextindexer
from plone import schema
from plone.app.textfield import RichText
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
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
        description=_(u'''
        Organizations that have provided funding for this item
        '''),
        default=[],
        value_type=RelationChoice(
            source=CatalogSource(portal_type='Organization'),
        ),
        required=False,
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
        title=u'Implementing Parnters',
        description=_(u'''
        Organizations that are implementing this item.
        '''),
        default=[],
        value_type=RelationChoice(
            source=CatalogSource(portal_type='Organization'),
        ),
        required=False,
    )

    # fieldset set the tabs on the edit form

    fieldset(
            'partners',
            label=_(u'Partners'),
            fields=[
                'donors',
                'implementing_partners',
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
    def implementing_partners(self):
        if safe_hasattr(self.context, 'implementing_partners'):
            return self.context.implementing_partners
        return None

    @implementing_partners.setter
    def implementing_partners(self, value):
        self.context.implementing_partners= value
