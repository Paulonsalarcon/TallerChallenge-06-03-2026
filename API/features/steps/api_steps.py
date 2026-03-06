import requests
from behave import given, when, then

@given('the API endpoint is "{endpoint}"')
def step_set_endpoint(context, endpoint):
    context.endpoint = endpoint

@when('I send a GET request to the endpoint')
def step_send_get_request(context):
    try:
        context.response = requests.get(context.endpoint)
    except requests.exceptions.RequestException as e:
        raise AssertionError(f"API Request failed: {e}")

@then('the response status code should be {status_code:d}')
def step_validate_status_code(context, status_code):
    actual_code = context.response.status_code
    assert actual_code == status_code, f"Validation Failed: Expected status code {status_code}, but got {actual_code}."

@then('the response JSON should contain the keys "{keys}"')
def step_validate_json_keys(context, keys):
    try:
        json_data = context.response.json()
    except ValueError:
        raise AssertionError("Validation Failed: The response is not valid JSON.")
    
    expected_keys = [key.strip() for key in keys.split(',')]
    for key in expected_keys:
        assert key in json_data, f"Validation Failed: Key '{key}' is missing from the JSON response."

@then('the value of the "{field}" field should be {expected_value:d}')
def step_validate_field_value(context, field, expected_value):
    json_data = context.response.json()
    actual_value = json_data.get(field)
    assert actual_value == expected_value, f"Validation Failed: Expected '{field}' to be {expected_value}, but got {actual_value}."