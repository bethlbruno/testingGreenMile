Feature: Smart Survey

  Scenario: Creating new form
    Given GreenMile is running #1
    When a User fill the Description, Organization, application rules and save the form
    Then GreenMile Service returns the updated form in the grid

#    Scenario: Searching for a created form
#      Given GreenMile is running #2
#      When a user searches for a pre existent form
#      Then GreenMile Service returns the one the user searched