from selenium.webdriver.common.by import By
from browser import Browser


class HomePage(Browser):
    # Locators
    LOGIN_BTN = (By.XPATH, ".//*[@id='about_8tracks_splash']/div[1]/div/div[2]/div[1]/a[1]")
    USERNAME_FIELD = (By.XPATH, ".//*[@id='login']")
    PASSWD_FIELD = (By.XPATH, ".//*[@id='password']")
    SUBMIT_BUTTON = (By.XPATH, ".//*[@id='login_form']/div/div[4]/input")

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def navigate(self, url):
        self.driver.get(url)
