from playwright.sync_api import sync_playwright

def test_browsers():
    browsers = [
        ("Chrome", "chromium"),
        ("Firefox", "firefox")
    ]
    all_passed = True
    for browser_name, browser_type in browsers:
        print(f" Тестируем в {browser_name}...")
        with sync_playwright() as p:
            # Выбираем тип браузера
            if browser_type == "chromium":
                browser = p.chromium.launch()
            else:
                browser = p.firefox.launch()
            page = browser.new_page()
            page.goto('https://playwright.dev/')
            title = page.title()
            expected = 'Fast and reliable end-to-end testing for modern web apps | Playwright'
            test_passed = title == expected
            all_passed = all_passed and test_passed
            print(f"Заголовок: {title}")
            print(f"Ожидаемый: {expected}")
            print(f"Тест пройден: {test_passed}")
            browser.close()
    if all_passed:
        print("Оба браузера работают корректно! Все тесты пройдены.")
    else:
        print("Некоторые тесты не пройдены")

if __name__ == "__main__":
    test_browsers()
