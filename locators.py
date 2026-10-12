from selenium.webdriver.common.by import By

class Main_Locators: # страница с кнопкой Войти в аккаунт
    LOG_BUTTON_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']") # кнопка Войти в аккаунт
    PLACE_AN_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']") # кнопка Оформить заказ
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']") # кнопка Личный кабинет
    BUN_TEXT = (By.XPATH, "//h2[text()='Булки']") # текст внутри раздела Булки
    SAUCES_TEXT = (By.XPATH, "//h2[text()='Соусы']") # текст внутри раздела Соусы
    FILLING_TEXT = (By.XPATH, "//h2[text()='Начинки']") # текст внутри раздела Начинки
    BUN_TAB = (By.XPATH, "//div[@style='display: flex;']//*[text()='Булки']") # вкладка Булки
    SAUCES_TAB = (By.XPATH, "//div[@style='display: flex;']//*[text()='Соусы']") # вкладка Соусы
    FILLING_TAB = (By.XPATH, "//div[@style='display: flex;']//*[text()='Начинки']") # вкладка Начинки



class Login_Locators: # страница с формой вход
    EMAIL_FIELD =(By.XPATH, ".//input[@type='text']") # поле Email
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']") # поле Пароль
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']") # кнопка Войти
    TEXT_REGISTER = (By.XPATH, ".//a[@href='/register']") # текст Зарегистрироваться
    TEXT_RESET_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']") # текст Восстановить пароль

class Register_Locators: # страница с формой регистрации
    NAME_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input") # поле Имя
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input") # поле Email
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input") # поле Пароль
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']") # кнопка Зарегистрироваться
    TEXT_LOGIN = (By.XPATH, "//a[@href='/login']") # текст Войти
    PASSWORD_ERROR = (By.XPATH, ".//*[text()='Некорректный пароль']") # текст Неккоректный пароль

class Forgot_Password_Locators: # страница восстановления пароля
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']") # кнопка Войти

class Login_Account_Locators: # страница в личном кабинете
    DESIGNER = (By.XPATH, "//a[./p[text()='Конструктор']]") # текст Конструктор в личном кабинете
    LOGO = (By.XPATH, ".//header//a[@href='/']") # логотип stella burgers
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выйти']") # кнопка Выйти
