from playwright.sync_api import Page, expect

def test_example(page, test_web_address):

    # We load a virtual browser and navigate to the /books page
    page.goto(f"http://{test_web_address}")

    # We look at the h1
    heading = page.locator("h1")

    # We assert that it has the the correct content
    expect(heading).to_have_text("User Management")

    # Assert that the user list includes the first user
    expect(page.locator("ul")).to_contain_text("john")

"""
Create User form adds a user to the list
"""
def test_form_happy_path(page, test_web_address):
    # We load a virtual browser and navigate to the /books page
    page.goto(f"http://{test_web_address}")

    page.get_by_label("Username").fill("Bob")
    page.get_by_role("button").click()

    # Assert that the user list now includes "Bob"
    expect(page.locator("ul")).to_contain_text("Bob")
