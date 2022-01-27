import asyncio
from playwright.async_api import Playwright, async_playwright


async def run(playwright: Playwright) -> None:
    try:
        # 30 seconds timeout w/devtools
        # browser = await playwright.chromium.launch(headless=False, devtools=True, slow_mo=30000)

        browser = await playwright.chromium.launch(headless=False, slow_mo=1000)
        context = await browser.new_context()

        # Open new page
        page = await context.new_page()

        # Go to https://app.cloud-logon.com/dev/calculator
        await page.goto("https://app.cloud-logon.com/dev/calculator")

        # Click input[name="submission"]
        await page.click("input[name=\"submission\"]")

        # Fill input[name="submission"]
        await page.fill("input[name=\"submission\"]", "1 + 1")

        # Press Enter
        await page.press("input[name=\"submission\"]", "Enter")
        # assert page.url == "https://app.cloud-logon.com/dev/calculator"

        # Click input[name="submission"]
        await page.click("input[name=\"submission\"]")

        # Fill input[name="submission"]
        await page.fill("input[name=\"submission\"]", "2 + 2")

        # Press Enter
        await page.press("input[name=\"submission\"]", "Enter")
        # assert page.url == "https://app.cloud-logon.com/dev/calculator"
    except KeyboardInterrupt as k:
        print('\nKeyboard exception received. Exiting ')
        raise k
    except Exception:
        print("\nUncaught exception occurred. Exiting ")
    finally:
        await context.close()
        await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
