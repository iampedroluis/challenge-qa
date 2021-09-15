class Registro:

    def __init__(self, driver):
        self.driver = driver
        #INPUTS DE REGISTRO
        self.nombre_usuario_r_xpath = "//input[@id='ap_customer_name']"
        self.email_usuario_r_xpath = "//input[@id='ap_email']"
        self.pass_usuario_r_xpath = "//input[@id='ap_password']"
        self.passcheck_usuario_r_xpath = "//input[@id='ap_password_check']"
        #BOTON CREAR CUENTA AMAZON
        self.boton_crearC_xpath = "//input[@id='continue']"


    #COMPLETAR LOS DATOS
    def completar_nombre(self, dato):
        #NOMBRE DE USUARIO
        self.driver.find_element_by_xpath(self.nombre_usuario_r_xpath).click()
        self.driver.find_element_by_xpath(self.nombre_usuario_r_xpath).clear()
        self.driver.find_element_by_xpath(self.nombre_usuario_r_xpath).send_keys(dato)


    #CORREO ELECTRONICO USUARIO
    def completar_email(self, dato):
        self.driver.find_element_by_xpath(self.email_usuario_r_xpath).click()
        self.driver.find_element_by_xpath(self.email_usuario_r_xpath).clear()
        self.driver.find_element_by_xpath(self.email_usuario_r_xpath).send_keys(dato)


    #CONTRASEÑA USUARIO
    def completar_contrasena(self, dato):
        self.driver.find_element_by_xpath(self.pass_usuario_r_xpath).click()
        self.driver.find_element_by_xpath(self.pass_usuario_r_xpath).clear()
        self.driver.find_element_by_xpath(self.pass_usuario_r_xpath).send_keys(dato)


    #CONFIRMACION CONTRASEÑA
    def check_pass_usr(self, dato):
        self.driver.find_element_by_xpath(self.passcheck_usuario_r_xpath).click()
        self.driver.find_element_by_xpath(self.passcheck_usuario_r_xpath).clear()
        self.driver.find_element_by_xpath(self.passcheck_usuario_r_xpath).send_keys(dato)


    #CLICK BOTON CREAR CUENTA

    def click_boton_crearC(self):
        self.driver.find_element_by_xpath(self.boton_crearC_xpath).click()

