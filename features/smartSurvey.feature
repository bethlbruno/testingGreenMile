Feature: Smart Survey

  Scenario: Creating new form
    Given GreenMile is running
    When a User fill the Description, Organization, application rules and save the form
    Then GreenMile Service returns the updated form in the grid