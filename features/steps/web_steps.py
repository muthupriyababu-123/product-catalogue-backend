
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I am on the "{page}"')
def step_impl(context, page):
    context.browser.get(context.base_url)


@when('I enter "{value}" in the "{field}" field')
def step_impl(context, value, field):
    field_ids = {
        "Name": "name",
        "Product ID": "product_id",
    }
    element = context.browser.find_element(By.ID, field_ids[field])
    element.clear()
    element.send_keys(value)


@when('I click the "{button}" button')
def step_impl(context, button):
    element = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            f"//button[normalize-space()='{button}']"
        ))
    )
    element.click()


@when('I clear the form')
def step_impl(context):
    context.browser.find_element(By.ID, "clear").click()


@when('I select "{value}" from the "{field}" list')
def step_impl(context, value, field):
    field_ids = {
        "Category": "category",
        "Availability": "available",
    }
    dropdown = Select(
        context.browser.find_element(By.ID, field_ids[field])
    )
    dropdown.select_by_visible_text(value)


@when('I copy the ID of product "{name}"')
def step_impl(context, name):
    rows = context.browser.find_elements(
        By.CSS_SELECTOR, "#search_results tbody tr"
    )
    for row in rows:
        if name in row.text:
            cells = row.find_elements(By.TAG_NAME, "td")
            context.product_id = cells[0].text.strip()
            return
    raise AssertionError(f"Product '{name}' was not found")


@when('I enter the copied ID in the "Product ID" field')
def step_impl(context):
    element = context.browser.find_element(By.ID, "product_id")
    element.clear()
    element.send_keys(context.product_id)


@when('I search for product "{name}"')
def step_impl(context, name):
    element = context.browser.find_element(By.ID, "name")
    element.clear()
    element.send_keys(name)
    context.browser.find_element(
        By.XPATH, "//button[normalize-space()='Search']"
    ).click()


@then('I should see the message "{message}"')
def step_impl(context, message):
    flash_message = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.ID, "flash_message"))
    )
    assert message in flash_message.text


@then('I should see "{text}" in the results')
def step_impl(context, text):
    results = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.ID, "search_results"))
    )
    assert text in results.text


@then('I should not see "{text}" in the results')
def step_impl(context, text):
    results = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.ID, "search_results"))
    )
    assert text not in results.text


@then('I should see the product "{name}"')
def step_impl(context, name):
    results = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.ID, "search_results"))
    )
    assert name in results.text


@then('I should see "{text}" in the product details')
def step_impl(context, text):
    details = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.ID, "product_details"))
    )
    assert text in details.text
