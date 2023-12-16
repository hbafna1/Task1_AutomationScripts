Feature: Pathology Lab Management web application scenarios

  # *** Using Background for the repetitive steps ***
  Background:
    When User enters valid Username
    And User enters valid Password
    And User clicks on Login button
    Then User will be able to Login into the application

# Scenario 1 / TC01
  Scenario: Login into Pathology Lab Management web application
    Given User opens the Pathology Lab Management web application

# Scenario 2 / TC02
  Scenario: After successful login, User will land on the home page of the application
    Given User opens the Pathology Lab Management web application
    When User lands on the home page they can view todos and access the Cost Calculator for blood tests
    Then User is able to view todos and access the Cost Calculator for blood tests

# Scenario 3 / TC03
  Scenario: Cost Calculator feature and apply discounts if applicable
    Given User opens the Pathology Lab Management web application
    When User selects its desired tests under Test Cost Calculator
    Then User should be able to select desired test under Test Cost Calculator
    When User clicks on Discount dropdown
    Then User should be able to select discount from dropdown which are applicable

# Scenario 4 / TC04
  Scenario: Adding Patients and Creating tests
    Given User opens the Pathology Lab Management web application
    When User clicks on Patients tab
    Then User navigates to Patients page
    When User clicks on Add Patient button
    Then User navigates to Add Patient form page
    When User enters all the required details in Patient Contact Details
    And User successfully enters all the required details in Patient Contact Details
    Then User clicks on General Details button to move on next page of the form
    When User moves to the next page of the form to fill required details in General Details
    And User successfully enters all the required details in General Details or Secondary Details
    Then User clicks on Add Tests button to move on next page of the form
    When User moves to the next page of the form to fill required details in Test Cost Calculator
    And User successfully enters all the required details in Test Cost Calculator
    Then User clicks on Add Patient button
    When After adding a test it will be reflected in the list of todos on the home page
    Then Validating that test is added in the list of todos on the home page
