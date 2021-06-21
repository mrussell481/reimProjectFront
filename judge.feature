Feature: Managers should be able to approve or deny requests and leave an optional comment

  Scenario: Approving a Request
    Given The user is a manager
    Given The manager is viewing a request
    When The manager types a comment
    When The manager presses the Approve button
    Then A message notifies the manager that the request's Approval Status was updated

  Scenario: Denying a Request
    Given The user is a manager
    Given The manager is viewing a request
    When The manager types a comment
    When The manager presses the Deny button
    Then A message tells the manager that the request's Approval Status was updated
