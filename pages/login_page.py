from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url , "Url adress for login is not correct"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def fill_registration_form(self, email, password):
        self.find(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.find(*LoginPageLocators.REGISTRATION_PASSWORD1).send_keys(password)
        self.find(*LoginPageLocators.REGISTRATION_PASSWORD2).send_keys(password)

    def submit_registration(self):
        self.find(*LoginPageLocators.REGISTRATION_SUBMIT).click()

    def should_be_message_about_registration(self):
        message = self.find(*LoginPageLocators.REGISTRATION_MESSAGE)
        assert  "Thanks for registering!" in message.text, "Should be message about registration"

