from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD_LOCATOR = By.XPATH, "//input[@placeholder='* Имя']"  # Поле ввода имени
    LASTNAME_FIELD_LOCATOR = By.XPATH, "//input[@placeholder='* Фамилия']"  # Поле ввода фамилии
    ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"  # Кнопка "Заказать"
    NEXT_BUTTON = By.XPATH, "//button[text()='Далее']"  # Кнопка "Далее"
    ADDRESS_FIELD = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"  # Поле ввода адреса
    STATION_FIELD = By.XPATH, "//input[@placeholder='* Станция метро']"  # Поле выбора метро
    STATION_DROPDOWN = By.XPATH, "//div[contains(@class, 'select-search__select')]/ul/li"  # Список метро
    PHONE_NUMBER_FIELD = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"  # Поле ввода номера
    COMMENT_FIELD = By.XPATH, "//input[@placeholder='Комментарий для курьера']"  # Поле комментария
    CONFIRM = By.XPATH, "//div[text()='Хотите оформить заказ?']"  # Диалог подтверждения
    YES_BUTTON = By.XPATH, "//button[text()='Да']"  # Кнопка "Да"
    DATE_FIELD = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"  # Поле ввода даты
    BLACK_CHECKBOX = By.ID, "black"  # Черный цвет
    GREY_CHECKBOX = By.ID, "grey"  # Серый цвет
    RENTAL_PERIOD = By.XPATH, "//div[@class='Dropdown-root']"  # Поле срока аренды
    RENTAL_PERIOD_DROPDOWN = By.XPATH, "//div[@class='Dropdown-menu']"  # Периоды
    ORDER_COMPLETED = By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"  # Информация о заказе
    ORDER_STATUS_BUTTON = By.XPATH, "//button[text()='Посмотреть статус']"  # Кнопка "Посмотреть статус"
    ONE_DAY = By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='сутки')]"  # День
    TWO_DAY = By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='двое суток')]"  # Два дня
    RENT_FORM = By.XPATH, "//div[text()='Про аренду']"  # Раздел "Про аренду"
    ORDER_BUTTON_IN_FOOTER = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"  # Кнопка "Заказать" на странице
    ORDER_BUTTON_IN_HEADER = By.XPATH, "//*[contains(@class, 'Header_Nav')]/button[text()='Заказать']"  # Кнопка "Заказать" в шапке

