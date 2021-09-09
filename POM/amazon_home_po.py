
class AmazonHome:


    def __init__(self,driver):
        self.driver = driver
        self.barra_busqueda_xpath = "//input[@id='twotabsearchtextbox']"
        self.boton_buscar_xpath = "//input[@id='nav-search-submit-button']"
        self.resultado_xpath = "//span[@class='a-color-state a-text-bold']"
        #CAMBIO DE CODIGO POSTAL
        self.enviar_a_xpath = "//a[@id='nav-global-location-popover-link']"
        self.input_codigo_p = "//input[@id='GLUXZipUpdateInput']"
        self.boton_aplicar_xpath = "//span[@id='GLUXZipUpdate']"
        self.boton_continuar_xpath = "/html/body/div[5]/div/div/div[2]/span"
        self.resultado_codigoP_xpath = "//span[@id='glow-ingress-line2']"
    def busqueda_producto(self, producto):
        self.driver.find_element_by_xpath(self.barra_busqueda_xpath).click()
        self.driver.find_element_by_xpath(self.barra_busqueda_xpath).clear()
        self.driver.find_element_by_xpath(self.barra_busqueda_xpath).send_keys(producto)

    def clic_buscar(self):
        self.driver.find_element_by_xpath(self.boton_buscar_xpath).click()

    def resultado_busqueda(self):
        self.driver.find_element_by_xpath(self.resultado_xpath)

#CAMBIO DE CODIGO POSTAL

    def envio_codigoP(self):
        self.driver.find_element_by_xpath(self.enviar_a_xpath).click() #hace click en enviar a

    def escribir_codigoPostal(self, codigopostal):  #ESCRIBE EL CODIGO POSTAL
        self.driver.find_element_by_xpath(self.input_codigo_p).click()
        self.driver.find_element_by_xpath(self.input_codigo_p).send_keys(codigopostal)

    def botton_aplicar(self): #BOTON APLICAR
        self.driver.find_element_by_xpath(self.boton_aplicar_xpath).click()

    def botton_continuar(self): #BOTON CONTINUAR
        self.driver.find_element_by_xpath(self.boton_continuar_xpath).click()

    def resultado_codigoPstal(self): #Resultado del cambio de codigo postal
        self.driver.find_element_by_xpath(self.resultado_codigoP_xpath)