from selenium.webdriver.common.keys import Keys


class BuscarGoogle:

    def __init__(self, driver):
        self.driver = driver
        #RUTA DE LA BARRA DE BUSQUEDA
        self.search_bar_xpath = "//input[@class='gLFyf gsfi']"
        #RUTA DEL LINK DE AMAZON
        self.search_link_xpath = "//h3[@class='LC20lb DKV0Md']"
    #BUSQUEDA DE GOOGLE
    def busqueda_google(self, palabra):
        self.driver.find_element_by_xpath(self.search_bar_xpath).click()
        self.driver.find_element_by_xpath(self.search_bar_xpath).clear()
        self.driver.find_element_by_xpath(self.search_bar_xpath).send_keys(palabra)
        self.driver.find_element_by_xpath(self.search_bar_xpath).send_keys(Keys.ENTER)
    #CLICK EN EL LINK DE AMAZON
    def click_amazon_link(self):
        self.driver.find_element_by_xpath(self.search_link_xpath).click()

