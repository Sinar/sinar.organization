# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from sinar.organization.testing import (
    SINAR_ORGANIZATION_FUNCTIONAL_TESTING,
    SINAR_ORGANIZATION_INTEGRATION_TESTING,
)
from zope.component import getMultiAdapter
from zope.interface.interfaces import ComponentLookupError
from zope.publisher.browser import TestRequest

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    """organization-view is registered with the addon's browser layer.

    The integration fixture's portal request provides the layer via the
    site skin, so the view resolves there.  A request without the layer
    must not match - there is no unlayered fallback registration.
    """

    layer = SINAR_ORGANIZATION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Organization', 'test-org')

    def test_organization_view_is_registered(self):
        view = getMultiAdapter(
            (self.portal['test-org'], self.portal.REQUEST),
            name='organization-view'
        )
        self.assertEqual(view.__name__, 'organization-view')

    def test_organization_view_requires_browser_layer(self):
        request = TestRequest('')
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['test-org'], request),
                name='organization-view'
            )

    def test_fti_registers_default_view(self):
        fti = self.portal.portal_types['Organization']
        self.assertEqual(fti.default_view, 'organization-view')
        self.assertIn('organization-view', fti.view_methods)


class ViewsFunctionalTest(unittest.TestCase):

    """With the browser layer active, organization-view is the
    registered default view of the Organization type."""

    layer = SINAR_ORGANIZATION_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Organization', 'test-org')

    def test_organization_view_is_registered(self):
        view = getMultiAdapter(
            (self.portal['test-org'], self.portal.REQUEST),
            name='organization-view'
        )
        self.assertEqual(view.__name__, 'organization-view')
