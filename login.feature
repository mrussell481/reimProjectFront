Feature: The user should be able to log in, and what they have access to should change depending on whether they're a Member or Manager

  Scenario: Log in as a Member
    Given The member is on the log in page
    When A member username is entered
    When A member password is entered
    When The Login button is pressed
    Then The main request page is loaded

  Scenario: Log in as a Manager
    Given The manager is on the log in page
    When A manager username is entered
    When A manager password is entered
    When The Login button is pressed
    Then The main request page is loaded
