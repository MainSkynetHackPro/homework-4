from pages.base_page import BasePage


class AuthPage(BasePage):
    EMAIL = '//input[@name="st.email"]'
    PASSWORD = '//input[@name="st.password"]'
    LOGIN_BUTTON = '//input[contains(@data-l, "sign_in")]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.EMAIL).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def login(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()
