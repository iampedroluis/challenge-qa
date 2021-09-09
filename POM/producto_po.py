class ProductoAmazon:

    def __init__(self, driver):
        self.driver = driver
        #COLORES
        self.casilla_color = "//li[@id='color_name_5']"
        self.resultado_xpath = "//span[@class='selection']"
        #TALLAS
        self.seleccion_tamano_xpath = "//*[@id='dropdown_selected_size_name']/span/span"
        self.talla_s_xpath = "//li[@id='size_name_1']"
        self.resultado_tamano_xpath = "//*[@id='dropdown_selected_size_name']/span/span/span[@class='a-dropdown-prompt']"
        #AGREGAR AL CARRITO
        self.boton_aggcarrito_xpath = "//input[@id='add-to-cart-button']"
        self.producto_carrito_xpath = "//span[@id='nav-cart-count']"
        #ELIMINAR DE LCARRITO
        self.boton_carrito_xpath = "//div[@id='nav-cart-count-container']/span[2]"
        self.boton_eliminar_xpath = "//span[@class='a-declarative']/input[@value='Eliminar']"

#COLORES
    def cambio_color(self):
        self.driver.find_element_by_xpath(self.casilla_color).click() #cambia de color

    def resultado_color(self):
        self.driver.find_element_by_xpath(self.resultado_xpath) #resultado del cambio de color
#TALLAS
    def selecotor_tamano(self):
        self.driver.find_element_by_xpath(self.seleccion_tamano_xpath).click() #selecciona la lista desplegable

    def tamano_s(self):
        self.driver.find_element_by_xpath(self.talla_s_xpath).click()#hace click en talla s

    def resultado_talla(self):
        self.driver.find_element_by_xpath(self.resultado_tamano_xpath)#resultado de eleccion de tamaño
#AGREGAR AL CARRITO
    def agregar_al_carrito(self):
        self.driver.find_element_by_xpath(self.boton_aggcarrito_xpath).click() #click boton agregar al carrito

    def resultado_carrito(self):
        self.driver.find_element_by_xpath(self.producto_carrito_xpath) #Resultado del carrito

#ELIMINAR DEL CARRITO
    def click_boton_carro(self):
        self.driver.find_element_by_xpath(self.boton_carrito_xpath).click()

    def click_eliminar_producto(self):
        self.driver.find_element_by_xpath(self.boton_eliminar_xpath).click()#CLICK EN ELIMINAR