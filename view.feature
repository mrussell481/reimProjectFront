Feature: The user should be able to click on any request on the list to view details

  Scenario: View Request as Member
    Given The user is a member
    When The user clicks on the Open button next to a request
    Then The page for that request is loaded

  Scenario: View Request as Manager
    Given The user is a manager
    When The user clicks on the Open button next to a request
    Then The page for that request is loaded