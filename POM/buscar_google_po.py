from selenium.webdriver.common.keys import Keys


class BuscarGoogle:

    def __init__(self, driver):
        self.driver = driver
        self.search_bar_xpath = "//input[@class='gLFyf gsfi']"
        self.search_link_xpath = "//h3[@class='LC20lb DKV0Md']"

    def busqueda_google(self, palabra):
        self.driver.find_element_by_xpath(self.search_bar_xpath).click()
        self.driver.find_element_by_xpath(self.search_bar_xpath).clear()
        self.driver.find_element_by_xpath(self.search_bar_xpath).send_keys(palabra)
        self.driver.find_element_by_xpath(self.search_bar_xpath).send_keys(Keys.ENTER)

    def click_amazon_link(self):
        self.driver.find_element_by_xpath(self.search_link_xpath).click()

