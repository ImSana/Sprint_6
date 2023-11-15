from selenium.webdriver.common.by import By


class MainPageLocators:
    FAQ = By.XPATH, "//div[contains(@class, 'Home_FAQ_')]"  # Раздел "Вопросы о важном"
    QUESTIONS = By.XPATH, "//div[contains(@class, 'accordion__item')]"  # Вопросы
    ANSWER = By.XPATH, "//div[contains(@class, 'accordion__panel') and not(@hidden)]"  # Отображаемый ответ
    COOKIE_BUTTON = By.XPATH, "//button[contains(@class, 'App_CookieButton_')]"  # Кнопка "Да все привыкли"

