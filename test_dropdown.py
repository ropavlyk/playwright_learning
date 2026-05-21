import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.smoke
@pytest.mark.regression
def test_standard_dropdown():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
        
            page.goto("https://demoqa.com/select-menu")

            page.locator("#oldSelectMenu").select_option("Black")

            expect(page.locator("#oldSelectMenu")).to_have_value("5")

            browser.close()


@pytest.mark.regression
def test_custom_dropdown():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
        
            page.goto("https://demoqa.com/select-menu")

            page.locator("#selectOne").click()
            page.locator("#react-select-3-option-0-1").click()
            expect(page.locator("#selectOne")).to_contain_text("Mr.")

            #page.wait_for_timeout(2000) 

            browser.close()


@pytest.mark.regression
def test_custom_multiselect_dropdown():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
        
            page.goto("https://demoqa.com/select-menu")

            page.locator("#react-select-4-input").click()
            page.locator("#react-select-4-option-2").click()
            page.locator("#react-select-4-option-3").click()

            expect(page.locator(".css-9jq23d", has_text="Black")).to_be_visible()
            expect(page.locator(".css-9jq23d", has_text="Red")).to_be_visible()

            browser.close()
