Feature: API Validation for JSONPlaceholder

  Scenario: Fetch a specific post and validate the response
    Given the API endpoint is "https://jsonplaceholder.typicode.com/posts/1"
    When I send a GET request to the endpoint
    Then the response status code should be 200
    And the response JSON should contain the keys "userId, id, title, body"
    And the value of the "id" field should be 1