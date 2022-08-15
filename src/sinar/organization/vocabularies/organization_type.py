# -*- coding: utf-8 -*-

from plone.dexterity.interfaces import IDexterityContent
# from plone import api
from sinar.organization import _
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class OrganizationType(object):
    """
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem(u'academe', _(u'Academia / Educational Institution')),
            VocabItem(u'bilateral',_(u'Bilateral Organization')),
            VocabItem(u'cso', _(u'Civil Society')),
            VocabItem(u'government-agency', _(u'Government Agency')),
            VocabItem(u'ingo', _(u'Intergovernmental Organization')),
            VocabItem(u'media',_(u'News or Media Organization')),
            VocabItem(u'private-sector', _(u'Private Sector / Business')),
            VocabItem(u'research', _(u'Research Institutions and Think Tanks')),
            VocabItem(u'trade-association', _(u'Trade Association or Union')),
        ]

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # NOQA: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token,
                    token=str(item.token),
                    title=item.value,
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


OrganizationTypeFactory = OrganizationType()
