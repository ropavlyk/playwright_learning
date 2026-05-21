import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.regression
def test_new_tab_opened():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto("https://demoqa.com/links")
        
            # watch and grab new tab
            with page.expect_popup() as new_tab:
                    page.get_by_role("link", name="Home", exact=True).click()

            # interact with new tab
            expect(new_tab.value).to_have_url("https://demoqa.com/")

            browser.close()


@pytest.mark.smoke
@pytest.mark.regression
def test_api_created():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto("https://demoqa.com/links")

            # intercept API response
            with page.expect_response("**/created") as response:
                   page.get_by_role("link", name="Created").click()

            # verify response status
            assert response.value.status == 201

            # verify message on the page
            expect(page.get_by_text("Link has responded with staus 201 and status text Created")).to_be_visible()

            # debugging the output
            # print(response.value.url)
            # print(response.value.status)

            browser.close()


@pytest.mark.regression
def test_api_forbidden():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto("https://demoqa.com/links")

            with page.expect_response("**/forbidden") as response:
                    page.get_by_role("link", name="Forbidden").click()

            assert response.value.status == 403
            expect(page.get_by_text("Link has responded with staus 403 and status text Forbidden")).to_be_visible()

            browser.close()


@pytest.mark.regression
def test_api_not_found():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto("https://demoqa.com/links")

            with page.expect_response("**/invalid-url") as response:
                    page.get_by_role("link", name="Not Found").click()

            assert response.value.status == 404
            expect(page.get_by_text("Link has responded with staus 404 and status text Not Found")).to_be_visible()

            browser.close()

