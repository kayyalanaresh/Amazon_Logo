Feature: View the Amazon logo
  Scenario: Logo Presence
    Given Browser Launch
    When Amazon Login Page
    Then Verify logo
    Then Browser Close
