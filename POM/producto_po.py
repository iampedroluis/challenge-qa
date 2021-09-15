import time
class ProductoAmazon:

    def __init__(self, driver):
        self.driver = driver
        #COLORES
        self.lista_colores_xpath = "//span[@id='dropdown_selected_color_name']"
        self.color_verde_xpath = "//option[@id='native_color_name_30']"
        #TALLAS
        self.seleccion_tamano_xpath = "//*[@id='dropdown_selected_size_name']/span/span"
        self.talla_m_xpath = "//a[@id='native_dropdown_selected_size_name_3']"
        #AGREGAR AL CARRITO
        self.boton_aggcarrito_xpath = "//input[@id='add-to-cart-button']"

        #ELIMINAR DE LCARRITO
        self.boton_carrito_xpath = "//div[@id='nav-cart-count-container']/span[2]"
        self.boton_eliminar_xpath = "//span[@class='a-declarative']/input[@value='Eliminar']"

#COLORES
    def cambio_color(self):
        self.driver.find_element_by_xpath(self.lista_colores_xpath).click() #cambia de color
        time.sleep(2)
        self.driver.find_element_by_xpath(self.color_verde_xpath).click()

#TALLAS
    def selecotor_tamano(self):
        self.driver.find_element_by_xpath(self.seleccion_tamano_xpath).click() #selecciona la lista desplegable

    def tamano_m(self):
        self.driver.find_element_by_xpath(self.talla_m_xpath).click()#hace click en talla s


#AGREGAR AL CARRITO
    def agregar_al_carrito(self):
        self.driver.find_element_by_xpath(self.boton_aggcarrito_xpath).click() #click boton agregar al carrito



#ELIMINAR DEL CARRITO
    def click_boton_carro(self):
        self.driver.find_element_by_xpath(self.boton_carrito_xpath).click()

    def click_eliminar_producto(self):
        self.driver.find_element_by_xpath(self.boton_eliminar_xpath).click()#CLICK EN ELIMINAR