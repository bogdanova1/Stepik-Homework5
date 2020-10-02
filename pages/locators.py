from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SHOW_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR,"#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR,"#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR,"#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR,"button[name = 'registration_submit']")
    REGISTRATION_MESSAGE = (By.CSS_SELECTOR,".alertinner")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "article h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "article .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner")