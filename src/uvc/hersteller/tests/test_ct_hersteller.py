# -*- coding: utf-8 -*-
from uvc.hersteller.content.hersteller import IHersteller  # NOQA E501
from uvc.hersteller.testing import UVC_HERSTELLER_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class HerstellerIntegrationTest(unittest.TestCase):

    layer = UVC_HERSTELLER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_hersteller_schema(self):
        fti = queryUtility(IDexterityFTI, name='Hersteller')
        schema = fti.lookupSchema()
        self.assertEqual(IHersteller, schema)

    def test_ct_hersteller_fti(self):
        fti = queryUtility(IDexterityFTI, name='Hersteller')
        self.assertTrue(fti)

    def test_ct_hersteller_factory(self):
        fti = queryUtility(IDexterityFTI, name='Hersteller')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IHersteller.providedBy(obj),
            u'IHersteller not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_hersteller_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Hersteller',
            id='hersteller',
        )

        self.assertTrue(
            IHersteller.providedBy(obj),
            u'IHersteller not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('hersteller', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('hersteller', parent.objectIds())

    def test_ct_hersteller_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Hersteller')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_hersteller_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Hersteller')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'hersteller_id',
            title='Hersteller container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
