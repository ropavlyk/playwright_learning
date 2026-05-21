import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.smoke
@pytest.mark.regression
def test_text_field(): 
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
    
        page.goto("https://demoqa.com/text-box")

        page.locator("#userName").fill("Roman Roman") 
        page.locator("#userEmail").fill("roman@example.com")
        page.locator("#currentAddress").fill("Vancouver")
        page.locator("#permanentAddress").fill("Calgary")
        
        page.get_by_role("button", name="Submit").click() 
        #page.locator("#submit").click()

        expect(page.get_by_text("Name:Roman Roman")).to_be_visible()
        expect(page.get_by_text("Email:roman@example.com")).to_be_visible()
        expect(page.get_by_text("Current Address :Vancouver")).to_be_visible()
        expect(page.get_by_text("Permananet Address :Calgary")).to_be_visible()
        
        browser.close()

