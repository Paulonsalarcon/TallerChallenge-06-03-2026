from behave import given, when, then
from pages.demoqaPage import TextBoxPage

@given('the user navigates to the DemoQA Text Box page')
def step_impl(context):
    context.text_box_page = TextBoxPage(context.page)
    context.text_box_page.go_to_page()

@when('the user enters full name "{name}"')
def step_impl(context, name):
    context.name = name # Store for validation later
    context.text_box_page.fill_input(TextBoxPage.FULL_NAME_INPUT, name)

@when('the user enters email "{email}"')
def step_impl(context, email):
    context.email = email
    context.text_box_page.fill_input(TextBoxPage.EMAIL_INPUT, email)

@when('the user enters current address "{address}"')
def step_impl(context, address):
    context.current_address = address
    context.text_box_page.fill_input(TextBoxPage.CURRENT_ADDRESS_INPUT, address)

@when('the user enters permanent address "{address}"')
def step_impl(context, address):
    context.permanent_address = address
    context.text_box_page.fill_input(TextBoxPage.PERMANENT_ADDRESS_INPUT, address)

@when('the user submits the form')
def step_impl(context):
    context.text_box_page.submit_form()

@then('the output should exactly match the submitted values')
def step_impl(context):
    output = context.text_box_page.get_output_text()
    
    assert f"Name:{context.name}" in output, f"Expected Name '{context.name}' not found in output"
    assert f"Email:{context.email}" in output, f"Expected Email '{context.email}' not found in output"
    assert f"Current Address :{context.current_address}" in output, f"Expected Current Address '{context.current_address}' not found in output"
    assert f"Permananet Address :{context.permanent_address}" in output, f"Expected Permanent Address '{context.permanent_address}' not found in output"