from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    main_page_link="http://selenium1py.pythonanywhere.com/"

    def __init__(self,browser):
        BasePage.__init__(self, browser, MainPage.main_page_link)

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*MainPageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"