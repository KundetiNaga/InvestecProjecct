Feature: To validate if R2-D2's skin color is white and blue
  Scenario Outline: Send get request and verify for for the R2-D2's skin color in the response payload
    Given the environment is ready for testing
    When the get request is send on the "<url>"
    Then the request is successful with the 200 message in the response
    Then verify R2-D2 skin color is white and blue in the response

    Examples:
    |             url              |
    | https://swapi.dev/api/people |
