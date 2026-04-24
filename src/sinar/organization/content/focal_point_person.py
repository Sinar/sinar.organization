# -*- coding: utf-8 -*-
from plone.app.dexterity import textindexer
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice, RelationList
from zope.interface import implementer


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
