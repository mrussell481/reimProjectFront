Feature: Members should be able to submit new bugs

  Scenario: Submitting a New Bug
    Given The user is a member
    When The member presses the Submit New Bug button
    Then The New Request page is loaded
    When The member enters a Bug Name
    When The member enters a Bug Description
    When the member presses the Submit button
    Then A message notifies the member that they successfully uploaded a new bug