Feature: As a user, I want to go to setting

Scenario: Go to setting
  Given Open sidebar
  When I clcik the setting button
  Then I go to setting page
  Then I should see "123"

