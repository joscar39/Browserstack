@regression
Feature: 01 Initial steps
  Background:
    Given Open the app Al Cambio

  Scenario: Init apk Al Cambio
    # TC81880: Initial Setup app al cambio
    Then Show Modal permits notification
    When Push allow permits notification
    Then Check modal of steps tutorial
    When Skin steps tutorial
    Then Validate logo app
