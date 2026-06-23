from playwright.sync_api import sync_playwright

print("START")

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=True
    )

    page = browser.new_page()

    print("OPENING HEROKU")

    page.goto(
        "https://the-internet.herokuapp.com/add_remove_elements/",
        timeout=60000
    )

    print("LOADED")

    print(page.title())

    browser.close()

print("DONE")