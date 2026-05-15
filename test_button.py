from playwright.sync_api import sync_playwright, expect

def test_button_click():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
        
            page.goto("https://demoqa.com/buttons")
            page.get_by_role("button", name="Click Me", exact=True).click()

            expect(page.get_by_text("You have done a dynamic click")).to_be_visible()

            browser.close()


def test_button_double_click():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
        
            page.goto("https://demoqa.com/buttons")
            page.get_by_role("button", name="Double Click Me").dblclick()

            expect(page.get_by_text("You have done a double click")).to_be_visible()

            browser.close()


def test_button_right_click():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
        
            page.goto("https://demoqa.com/buttons")

            page.get_by_role("button", name="Right Click Me").click(button="right")

            expect(page.get_by_text("You have done a right click")).to_be_visible()

            browser.close()

