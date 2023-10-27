# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from sinar.organization.content.focal_point_person import IFocalPointPerson  # NOQA E501
from sinar.organization.testing import SINAR_ORGANIZATION_INTEGRATION_TESTING  # noqa
from zope.component import createObject, queryUtility

import unittest


class FocalPointPersonIntegrationTest(unittest.TestCase):

    layer = SINAR_ORGANIZATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_focal_point_person_schema(self):
        fti = queryUtility(IDexterityFTI, name='Focal Point Person')
        schema = fti.lookupSchema()
        self.assertEqual(IFocalPointPerson, schema)

    def test_ct_focal_point_person_fti(self):
        fti = queryUtility(IDexterityFTI, name='Focal Point Person')
        self.assertTrue(fti)

    def test_ct_focal_point_person_factory(self):
        fti = queryUtility(IDexterityFTI, name='Focal Point Person')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IFocalPointPerson.providedBy(obj),
            u'IFocalPointPerson not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_focal_point_person_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Focal Point Person',
            id='focal_point_person',
        )

        self.assertTrue(
            IFocalPointPerson.providedBy(obj),
            u'IFocalPointPerson not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('focal_point_person', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('focal_point_person', parent.objectIds())

    def test_ct_focal_point_person_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Focal Point Person')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_focal_point_person_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Focal Point Person')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'focal_point_person_id',
            title='Focal Point Person container',
        )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type='Document',
            title='My Content',
        )
        self.assertTrue(
            obj,
            u'Cannot add {0} to {1} container!'.format(obj.id, fti.id)
        )
