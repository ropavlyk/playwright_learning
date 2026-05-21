import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.smoke
@pytest.mark.regression
def test_yes_radio_button(): 
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
    
        page.goto("https://demoqa.com/radio-button")

        page.locator("#yesRadio").click()
        expect(page.get_by_text("You have selected Yes")).to_be_visible()
        
        browser.close()


@pytest.mark.regression
def test_impressive_radio_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
    
        page.goto("https://demoqa.com/radio-button")

        #page.locator("#impressiveRadio").click()
        page.get_by_role("radio", name="Impressive").click()
        expect(page.get_by_text("You have selected Impressive")).to_be_visible()

        browser.close()


@pytest.mark.regression
def test_disabled_radio_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
    
        page.goto("https://demoqa.com/radio-button")
        expect(page.locator("#noRadio")).to_be_disabled()

        browser.close()

        #run in terminal: pytest Learning/test_radio_button.py -v