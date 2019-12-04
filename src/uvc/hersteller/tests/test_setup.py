# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from uvc.hersteller.testing import UVC_HERSTELLER_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that uvc.hersteller is properly installed."""

    layer = UVC_HERSTELLER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if uvc.hersteller is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'uvc.hersteller'))

    def test_browserlayer(self):
        """Test that IUvcHerstellerLayer is registered."""
        from uvc.hersteller.interfaces import (
            IUvcHerstellerLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IUvcHerstellerLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = UVC_HERSTELLER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['uvc.hersteller'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if uvc.hersteller is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'uvc.hersteller'))

    def test_browserlayer_removed(self):
        """Test that IUvcHerstellerLayer is removed."""
        from uvc.hersteller.interfaces import \
            IUvcHerstellerLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IUvcHerstellerLayer,
            utils.registered_layers())
