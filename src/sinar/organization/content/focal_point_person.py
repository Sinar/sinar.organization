# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
try:
    from plone.app.dexterity import textindexer
except ImportError:
    from collective import dexteritytextindexer as textindexer
from plone.app.z3cform.widget import RelatedItemsFieldWidget, SelectFieldWidget
from z3c.relationfield.schema import RelationChoice, RelationList
from Products.ZCatalog.interfaces import IZCatalog
from plone.autoform.interfaces import IFormFieldProvider
from plone.indexer.interfaces import IIndexer
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from plone.app.vocabularies.catalog import CatalogSource

# from sinar.organization import _


class IFocalPointPerson(model.Schema):
    """ Marker interface and Dexterity Python Schema for FocalPointPerson
    """
    textindexer.searchable('partner')
    directives.widget('partner',
                      RelatedItemsFieldWidget,
                      pattern_options={
                          'basePath': '/',
                          'mode': 'auto',
                          'favourites': [],
                      }
                      )
    partner = RelationList(
        title='Related organization(s)',
        description='Organization(s) related to this person',
        required=False,
        value_type=RelationChoice(
            source=CatalogSource(portal_type='Organization'),
        ),
    )

    textindexer.searchable('project')
    directives.widget('project',
                      RelatedItemsFieldWidget,
                      pattern_options={
                          'basePath': '/',
                          'mode': 'auto',
                          'favourites': [],
                      }
                      )

    project = RelationList(
        title='Related project(s)',
        description='Project(s) related to this person',
        required=False,
        value_type=RelationChoice(
            source=CatalogSource(portal_type='Project'),
        ),
    )

@implementer(IFocalPointPerson)
class FocalPointPerson(Container):
    """ Content-type class for IFocalPointPerson
    """
