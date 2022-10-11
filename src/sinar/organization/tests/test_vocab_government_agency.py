# -*- coding: utf-8 -*-
from plone.app.testing import setRoles, TEST_USER_ID
from sinar.organization import _
from sinar.organization.testing import SINAR_ORGANIZATION_INTEGRATION_TESTING  # noqa
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory, IVocabularyTokenized

import unittest


class GovernmentAgencyIntegrationTest(unittest.TestCase):

    layer = SINAR_ORGANIZATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_vocab_government_agency(self):
        vocab_name = 'sinar.organization.GovernmentAgency'
        factory = getUtility(IVocabularyFactory, vocab_name)
        self.assertTrue(IVocabularyFactory.providedBy(factory))

        vocabulary = factory(self.portal)
        self.assertTrue(IVocabularyTokenized.providedBy(vocabulary))
        self.assertEqual(
            vocabulary.getTerm('sony-a7r-iii').title,
            _(u'Sony Aplha 7R III'),
        )
