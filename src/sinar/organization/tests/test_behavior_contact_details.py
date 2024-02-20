# -*- coding: utf-8 -*-
from plone.app.testing import setRoles, TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from sinar.organization.behaviors.contact_details import IContactDetailsMarker
from sinar.organization.testing import SINAR_ORGANIZATION_INTEGRATION_TESTING  # noqa
from zope.component import getUtility

import unittest


class ContactDetailsIntegrationTest(unittest.TestCase):

    layer = SINAR_ORGANIZATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_contact_details(self):
        behavior = getUtility(IBehavior, 'sinar.organization.contact_details')
        self.assertEqual(
            behavior.marker,
            IContactDetailsMarker,
        )
