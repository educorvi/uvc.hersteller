# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import uvc.hersteller


class UvcHerstellerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=uvc.hersteller)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'uvc.hersteller:default')


UVC_HERSTELLER_FIXTURE = UvcHerstellerLayer()


UVC_HERSTELLER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(UVC_HERSTELLER_FIXTURE,),
    name='UvcHerstellerLayer:IntegrationTesting',
)


UVC_HERSTELLER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(UVC_HERSTELLER_FIXTURE,),
    name='UvcHerstellerLayer:FunctionalTesting',
)


UVC_HERSTELLER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        UVC_HERSTELLER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='UvcHerstellerLayer:AcceptanceTesting',
)
