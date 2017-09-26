from selenium import webdriver


class Browser(object):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()
