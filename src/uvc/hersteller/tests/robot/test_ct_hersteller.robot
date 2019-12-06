# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s uvc.hersteller -t test_hersteller.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src uvc.hersteller.testing.UVC_HERSTELLER_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/uvc/hersteller/tests/robot/test_hersteller.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Hersteller
  Given a logged-in site administrator
    and an add Hersteller form
   When I type 'My Hersteller' into the title field
    and I submit the form
   Then a Hersteller with the title 'My Hersteller' has been created

Scenario: As a site administrator I can view a Hersteller
  Given a logged-in site administrator
    and a Hersteller 'My Hersteller'
   When I go to the Hersteller view
   Then I can see the Hersteller title 'My Hersteller'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Hersteller form
  Go To  ${PLONE_URL}/++add++Hersteller

a Hersteller 'My Hersteller'
  Create content  type=Hersteller  id=my-hersteller  title=My Hersteller

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Hersteller view
  Go To  ${PLONE_URL}/my-hersteller
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Hersteller with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Hersteller title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
