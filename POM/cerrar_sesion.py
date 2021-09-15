class CerrarSesion:

    def __init__(self, driver):
        self.driver = driver
        #RUTA MENU HAMBURGUESA AMAZON
        self.menu_hamburguesa_xpath = "//a[@id='nav-hamburger-menu']"
        #RUTA BOTON SALIR
        self.salir_boton_xpath = "//*[@id='hmenu-content']/ul[1]/li[35]/a"

    #CLICK EN MENU HAMBURGUESA
    def click_menu_hamb(self):
        self.driver.find_element_by_xpath(self.menu_hamburguesa_xpath).click()
    #CLICK EN BOTON SALIR
    def click_boton_salir(self):
        self.driver.find_element_by_xpath(self.salir_boton_xpath).click()


