# -*- coding: utf-8 -*-
from sinar.organization.behaviors.partners import IPartnersMarker
from sinar.organization.testing import SINAR_ORGANIZATION_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class PartnersIntegrationTest(unittest.TestCase):

    layer = SINAR_ORGANIZATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_partners(self):
        behavior = getUtility(IBehavior, 'sinar.organization.partners')
        self.assertEqual(
            behavior.marker,
            IPartnersMarker,
        )
