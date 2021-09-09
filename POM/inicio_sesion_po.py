class InicioSesion:

    def __init__(self, driver):
        self.driver = driver
        self.email_usuario_is_xpath = "//input[@id='ap_email']"
        self.boton_continuar_is_xpath = "//*[@id='continue']"
        self.pass_usuario_is_xpath = "//input[@id='ap_password']"
        self.boton_iniciarS_is_xpath = "//input[@id='signInSubmit']"

    # ESCRIBIR EMAIL
    def escribirmail(self, email):
        self.driver.find_element_by_xpath(self.email_usuario_is_xpath).click()
        self.driver.find_element_by_xpath(self.email_usuario_is_xpath).clear()
        self.driver.find_element_by_xpath(self.email_usuario_is_xpath).send_keys(email)

    # CLICK BOTON CONTINUAR
    def click_continuar_is(self):
        self.driver.find_element_by_xpath(self.boton_continuar_is_xpath).click()

    # ESCIRBIR CONTRASEÑA
    def escribircontrasena(self, contrasena):
        self.driver.find_element_by_xpath(self.pass_usuario_is_xpath).click()
        self.driver.find_element_by_xpath(self.pass_usuario_is_xpath).clear()
        self.driver.find_element_by_xpath(self.pass_usuario_is_xpath).send_keys(contrasena)

    #BOTON CONTINUAR
    def click_boton_is(self):
        self.driver.find_element_by_xpath(self.boton_iniciarS_is_xpath).click()