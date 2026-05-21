import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.smoke
@pytest.mark.regression
def test_checkbox_checks():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
        
            page.goto("https://demoqa.com/checkbox")
            page.get_by_role("checkbox", name="Select Home").check()
            #page.get_by_label("Home").click()

            expect(page.get_by_text("You have selected :home")).to_be_visible()

            browser.close()


@pytest.mark.regression
def test_checkbox_unchecks():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
        
            page.goto("https://demoqa.com/checkbox")
            page.get_by_role("checkbox", name="Select Home").click()
            expect(page.get_by_text("You have selected :home")).to_be_visible()
            page.get_by_role("checkbox", name="Select Home").click()
            expect(page.get_by_text("You have selected :home")).not_to_be_visible()

            browser.close()


@pytest.mark.regression
def test_tree_expands():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
        
            page.goto("https://demoqa.com/checkbox")
            page.locator(".rc-tree-switcher").click() 
            expect(page.get_by_role("checkbox", name="Select Desktop")).to_be_visible()

            browser.close()


@pytest.mark.regression
def test_tree_collapses():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
        
            page.goto("https://demoqa.com/checkbox")
            page.locator(".rc-tree-switcher").click()
            expect(page.get_by_role("checkbox", name="Select Desktop")).to_be_visible()
            page.locator(".rc-tree-switcher_open").click()
            expect(page.get_by_role("checkbox", name="Select Desktop")).not_to_be_visible()

            browser.close()


@pytest.mark.regression
def test_sub_checkbox_checks():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto("https://demoqa.com/checkbox")
            page.locator(".rc-tree-switcher").click() 
            expect(page.get_by_role("checkbox", name="Select Desktop")).to_be_visible()
            page.get_by_role("checkbox", name="Select Desktop").click()
            expect(page.get_by_text("You have selected :desktop")).to_be_visible()

            browser.close()