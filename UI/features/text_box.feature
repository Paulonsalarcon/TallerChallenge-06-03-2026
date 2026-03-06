Feature: DemoQA Text Box Form

  Scenario: Fill and submit the text box form successfully
    Given the user navigates to the DemoQA Text Box page
    When the user enters full name "John Doe"
    And the user enters email "john.doe@example.com"
    And the user enters current address "123 Main St"
    And the user enters permanent address "456 Secondary St"
    And the user submits the form
    Then the output should exactly match the submitted values