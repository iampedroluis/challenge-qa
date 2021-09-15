import unittest

class Asserts:

    def __init__(self, driver):
        #XPATHS
        self.driver = driver
        #ALERTA DEL NOMBRE FALTANTE
        self.alerta_nombre = "//*[@id='auth-customerName-missing-alert']/div/div"
        #ALERTA DEL EMAIL FALTANTE
        self.alerta_email = "//*[@id='auth-email-missing-alert']/div/div"
        #ALERTA DE DATO FALTANTE
        self.alerta_dato_is = "//*[@id='auth-email-missing-alert']/div/div"
        #ALERTA DE PASSWORD FALTANTE
        self.alerta_pass_is = "//*[@id='auth-password-missing-alert']/div/div"
        #ALERTA DE ERROR DE PASSWORD
        self.alerta_error_pass = "//*[@id='auth-error-message-box']/div/div/ul/li/span"
        #RESULTADO DE BUSQUEDA
        self.resultado_busqueda_xpath = "//span[@class='a-color-state a-text-bold']"
        #RESULTADO DE COLOR
        self.resultado_color_xpath = "//option[@id='native_color_name_30']"
        #RESULTADO DE TAMAÑO
        self.resultado_tamano_xpath = "//span[@id='dropdown_selected_size_name']"
        #RESULTADO DE CODIGO POSTAL
        self.resultado_codigoP_xpath = "//span[@id='glow-ingress-line2']"
        #PRODUCTO CARRITO
        self.producto_carrito_xpath = "//span[@id='nav-cart-count']"
        #RESULTADO ENVIO MAIL
        self.envio_mail_xpath = "//*[@id='verification-code-form']/div[4]/div[1]/h1"
        #DESLOGEO DE CUENTA
        self.titulo_iniciar_xpath = "//*[@id='authportal-main-section']/div[2]/div/div[1]/form/div/div/div/h1"

#FUNCIONES DE LOS ASSERTS:

    #ASSERT DEL TITULO DE LA PAGINA DE AMAZON
    def titulo(self):
        self.string_titulo = "Amazon.com. Gasta menos. Sonríe más."
        self.get_title = self.driver.title
        assercion = unittest.TestCase('__init__')
        assercion.assertEqual(self.get_title, self.string_titulo)

    #ASSERT DEL RESULTADO DE BUSQUEDA
    def resultado_busqueda(self):
        self.string_producto = '"sudaderas de hombre champion"'
        self.texto_producto = self.driver.find_element_by_xpath(self.resultado_busqueda_xpath).text
        assercion = unittest.TestCase('__init__')
        assercion.assertEqual(self.texto_producto, self.string_producto)

    #ASSERT DEL CAMBIO DE COLOR
    def resultado_color(self):
        self.string_color = "Rockin Teal-y07718"
        self.resultado_text_color = self.driver.find_element_by_xpath(self.resultado_color_xpath).text  # resultado del cambio de color
        assercion = unittest.TestCase('__init__')
        assercion.assertEqual(self.string_color, self.resultado_text_color)

    #ASSERT DE CAMBIO DE TALLA
    def resultado_talla(self):
        self.string_talla = "M"
        self.resultado_talla_m = self.driver.find_element_by_xpath(self.resultado_tamano_xpath).text#resultado de eleccion de tamaño
        assercion = unittest.TestCase('__init__')
        assercion.assertEqual(self.string_talla, self.resultado_talla_m)

    #ASSERT CAMBIO DE CODIGO POSTAL
    def resultado_codigoPostal(self): #Resultado del cambio de codigo postal
        self.string_CodigoP = "Miami 33101‌"
        self.resultado_codigoP = self.driver.find_element_by_xpath(self.resultado_codigoP_xpath).text
        assercion = unittest.TestCase('__init__')
        assercion.assertEqual(self.string_CodigoP, self.resultado_codigoP)

    #ASSERT CARRITO CON PRODUCTO
    def resultado_carrito_con_producto(self):
        self.string_carrito = "1"
        self.resultado_carrito = self.driver.find_element_by_xpath(self.producto_carrito_xpath).text #Resultado del carrito
        assercion = unittest.TestCase('__init__')
        assercion.assertEqual(self.string_carrito, self.resultado_carrito)

    #ASSERT CARRITO SIN PRODUCTO
    def resultado_carrito_sin_producto(self):
        self.string_carrito = "0"
        self.resultado_carrito = self.driver.find_element_by_xpath(self.producto_carrito_xpath).text  # Resultado del carrito
        assercion = unittest.TestCase('__init__')
        assercion.assertEqual(self.string_carrito, self.resultado_carrito)
    #ASSERT ENVIO DE MAIL REGISTRO
    def resultado_envia_mail(self):
        self.string_validacion_mail = "Verificar dirección de correo electrónico"
        self.resultado_mail = self.driver.find_element_by_xpath(self.envio_mail_xpath).text
        assercion = unittest.TestCase('__init__')
        assercion.assertEqual(self.string_validacion_mail, self.resultado_mail)

    #ASSERT DESLOGEO DE CUENTA
    def sesion_out(self):
        self.string_deslog = "Sign-In"
        self.resultado_deslog = self.driver.find_element_by_xpath(self.titulo_iniciar_xpath).text
        assercion = unittest.TestCase('__init__')
        assercion.assertEqual(self.string_deslog, self.resultado_deslog)
    
    #ASSERT ALERTA FALTA NOMBRE REGISTRO
    def alertname(self):
        self.string_alerta_n = "Introduce tu nombre"
        self.resultado_alerta_n = self.driver.find_element_by_xpath(self.alerta_nombre).text
        assercion = unittest.TestCase('__init__')
        assercion.assertEqual(self.string_alerta_n, self.resultado_alerta_n)
    #ASSERT ALERTA FALTA E-MAIL REGISTRO 
    def alertmail(self):
        self.string_alerta_e = "Introduce tu email"
        self.resultado_alerta_e = self.driver.find_element_by_xpath(self.alerta_email).text
        assercion = unittest.TestCase('__init__')
        assercion.assertEqual(self.string_alerta_e, self.resultado_alerta_e)
        
    # ASSERT FALTA NOMBRE INICIO SESION
    def alertisnombre(self):
        self.string_alerta_n_is = "Enter your email or mobile phone number"
        self.resultado_nombre_is = self.driver.find_element_by_xpath(self.alerta_dato_is).text
        assercion = unittest.TestCase('__init__')
        assercion.assertEqual(self.string_alerta_n_is, self.resultado_nombre_is)
    #ASSERT FALTA DE PASSWORD INISIO SESION
    def alertaispass(self):
        self.string_pass_is = "Enter your password"
        self.resultado_pass_is = self.driver.find_element_by_xpath(self.alerta_pass_is).text
        assercion = unittest.TestCase('__init__')
        assercion.assertEqual(self.string_pass_is, self.resultado_pass_is)

    #ASSERT PASSWORD INCORRECTA
    def alerta_pass_incorrect(self):
        self.string_pass_incorrect = "Your password is incorrect"
        self.resultado_pass_incorrect = self.driver.find_element_by_xpath(self.alerta_error_pass).text
        assercion = unittest.TestCase('__init__')
        assercion.assertEqual(self.string_pass_incorrect, self.resultado_pass_incorrect)
        
        



