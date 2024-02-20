# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s sinar.organization -t test_focal_point_person.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src sinar.organization.testing.SINAR_ORGANIZATION_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/sinar/organization/tests/robot/test_focal_point_person.robot
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

Scenario: As a site administrator I can add a Focal Point Person
  Given a logged-in site administrator
    and an add Focal Point Person form
   When I type 'My Focal Point Person' into the title field
    and I submit the form
   Then a Focal Point Person with the title 'My Focal Point Person' has been created

Scenario: As a site administrator I can view a Focal Point Person
  Given a logged-in site administrator
    and a Focal Point Person 'My Focal Point Person'
   When I go to the Focal Point Person view
   Then I can see the Focal Point Person title 'My Focal Point Person'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Focal Point Person form
  Go To  ${PLONE_URL}/++add++Focal Point Person

a Focal Point Person 'My Focal Point Person'
  Create content  type=Focal Point Person  id=my-focal_point_person  title=My Focal Point Person

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Focal Point Person view
  Go To  ${PLONE_URL}/my-focal_point_person
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Focal Point Person with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Focal Point Person title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
