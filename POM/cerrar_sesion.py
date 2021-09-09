class CerrarSesion:

    def __init__(self, driver):
        self.driver = driver
        self.menu_hamburguesa_xpath = "//a[@id='nav-hamburger-menu']"
        self.salir_boton_xpath = "//*[@id='hmenu-content']/ul[1]/li[35]/a"
        self.titulo_iniciar_xpath = "//*[@id='authportal-main-section']/div[2]/div/div[1]/form/div/div/div/h1"

    def click_menu_hamb(self):
        self.driver.find_element_by_xpath(self.menu_hamburguesa_xpath).click()

    def click_boton_salir(self):
        self.driver.find_element_by_xpath(self.salir_boton_xpath).click()

    def sesion_out(self):
        self.driver.find_element_by_xpath(self.titulo_iniciar_xpath)
