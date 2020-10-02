from pages.main_page import MainPage
from pages.login_page import LoginPage
from datetime import datetime

class TestRegistrationNewUser:
    def test_registration_new_user(self,browser):
        now = datetime.now().strftime('%Y%m%d_%H%M%S')
        password = "P"+now
        email = password + "@test.com"

        page = MainPage(browser)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.should_be_register_form()

        login_page.fill_registration_form(email, password)
        login_page.submit_registration()

        login_page.should_be_message_about_registration()





