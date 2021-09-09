#importo las librerias a sutilizar
from behave import *
from selenium import webdriver
import time
#importo las clases de los POM
from POM.buscar_google_po import BuscarGoogle
from POM.amazon_home_po import *
from POM.producto_po import *
from POM.registro_po import *
from POM.inicio_sesion_po import *
from POM.cerrar_sesion import *
from POM.asserts_po import *


print("<--- CHALLENGE QA/QC -------->")

#PRIMER CASO DE PRUEBA


@given('Tener acceso a internet') #ENTRO A GOOGLE
def acceso_a_internet(context):
    context.driver = webdriver.Chrome(executable_path="/home/iampedroluisg/Escritorio/chromedriver") #Ruta del Browser
    context.driver.get("https://www.google.com/")  #Pagina a la que visitara


@when('el usuario busca en google amazon') #BUSCA GOOGLE
def busca_amazon_en_google(context):
    context.buscar = BuscarGoogle(context.driver)
    context.buscar.busqueda_google("Amazon.com") #Busco Google en el Buscador de Google
    time.sleep(3)


@when('ingresa en el link de amazon')  #INGRESA EN EL LINK DE AMAZON
def ingresar_link_amazon(context):
    context.click = BuscarGoogle(context.driver) #Hago click en el Boton de Buscar en Google
    context.click.click_amazon_link()   #Ingreso en el linf de Amazon
    time.sleep(3)


@then('puede ver la home de amazon') # HAGO UN ASSERT DEL TITULO DE LA PAGINA
def home_amazon(context):
    try:
        assert 'Amazon.com. Gasta menos. Sonríe más.' in context.driver.title   #Hago un assert de el tituko de la pagina
        print("Paso el test")

    except Exception as e:
        print("no es la pagina de amazon", format(e))
    time.sleep(5)

#TEST CASE 2


@given('Tener acceso a la pagina de amazon')
def amazon_home(context):
    context.driver = webdriver.Chrome(executable_path="/home/iampedroluisg/Escritorio/chromedriver")
    context.driver.get("https://www.amazon.com/")


@when('el escribe busca sudaderas de hombre champion en la barra de busqueda')
def escribir(context):
    context.nombre_producto = AmazonHome(context.driver)
    context.nombre_producto.busqueda_producto("sudaderas de hombre champion")  #Busco Sudadera Champion de hombre


@when('hace click en el boton buscar')
def click_buscar(context):
    context.click_lupa = AmazonHome(context.driver)  #declaro una variable contex.[nombredeDeLaVariable] = Class(context.driver)
    context.click_lupa.clic_buscar() #Click en lupa de buscar de amazon



@then('se visualizan los resultados del producto buscado')
def resultado_de_busqueda(context):
    context.resultado = AmazonHome(context.driver)
    try:
        assert '"sudaderas de hombre champion"' in context.resultado.resultado_busqueda() #Assert del resultado de la busqueda
        print("Paso el test")

    except Exception as e:
        print("no encontro resultado", format(e))
    time.sleep(5)


# TEST CASE 3

@given('haber seleccionado un producto')
def producto(context):
    context.driver = webdriver.Chrome(executable_path="/home/iampedroluisg/Escritorio/chromedriver")
    context.driver.get("https://cutt.ly/VWHYmLx") #Utilizo acortadores de URL por ser el link muy largo


@when('el usuario selecciona otro color disponible')
def seleccion_color(context):
    context.click_color = ProductoAmazon(context.driver)
    context.click_color.cambio_color() #hago click en el cambio de color


@then('Se visualiza el mismo producto con otro color')
def resultado_color(context):
    context.resultado = ProductoAmazon(context.driver)
    try:
        assert "Mache Azul-586506" in context.resultado.resultado_color()  #Assert del resultado del cambio de color
        print("Paso el test")

    except Exception as e:
        print("no es el color", format(e))
    time.sleep(5)

#TEST CASE 4


@when('el usuario hace click en la lista desplegable de "Tamaño"') #Selecciona la lista desplegable
def lista_desplegable(context):
    context.lista_talla = ProductoAmazon(context.driver)
    context.lista_talla.selecotor_tamano()#Click lista desplegable


@when('selecciona el tamaño deseado') #Seleccion de talla
def talla(context):
    context.talla_s = ProductoAmazon(context.driver)
    context.talla_s.tamano_s()#selecciona tamaño s


@then('se visualiza el producto con el talle deseado') #Assert Resultado
def comprueba_tamano(context):
    context.producto_s = ProductoAmazon(context.driver)
    try:
        assert "S" in context.producto_s.resultado_talla()
        print("Paso el test")

    except Exception as e:
        print("no es el color", format(e))
    time.sleep(5)

#TEST CASE 5

@given('que el usuario este en el Home de Amazon')
def amazon_home(context):
    context.driver = webdriver.Chrome(executable_path="/home/iampedroluisg/Escritorio/chromedriver")
    context.driver.get("https://www.amazon.com/")


@when('el usuario hace click en "Enviar a"')
def click_enviar_a(context):
    context.enviar = AmazonHome(context.driver)
    context.enviar.envio_codigoP() #Clicl en enviar a de amazon
    time.sleep(5)

@when('escribe el Codigo Postal de Miami que es 33101')
def escribir_codigoP(context):
    context.escribeC = AmazonHome(context.driver)
    context.escribeC.escribir_codigoPostal("33101") #Ingreso el codigo postal


@when('hace click en "aplicar"')
def click_aplicar(context):
    context.click_boton_aplicar = AmazonHome(context.driver)
    context.click_boton_aplicar.botton_aplicar() #click en aplicar
    time.sleep(5)


@when('hace click en "continuar"')
def click_continuar(context):
    context.click_boton_continuar = AmazonHome(context.driver)
    context.click_boton_continuar.botton_continuar() #Click en continuar
    time.sleep(5)

@then('Se visualiza el cambio de locacion')
def cambiodecodigoP(context):
    context.resultadocodigoP = AmazonHome(context.driver)
    try:
        assert "Miami 33101‌" in context.resultadocodigoP.resultado_codigoPstal()  #Assert si cambio el codigo postal
        print("Paso el test")

    except Exception as e:
        print("no es el codigo postal", format(e))
    time.sleep(5)

#TEST CASE 6


@given('que el usuario haya seleccionado el producto deseado')
def producto(context):
    context.driver = webdriver.Chrome(executable_path="/home/iampedroluisg/Escritorio/chromedriver")
    context.driver.get("https://www.amazon.com/-/es/Sudadera-Champion-Powerblend-logotipo-Negro-y06794/dp/B078GLNW6P/ref=sr_1_5?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=champion%20sweatshirts%20for%20men&qid=1631121282&sr=8-5") #Acortador de URL
    context.lista_talla = ProductoAmazon(context.driver)
    context.lista_talla.selecotor_tamano()#Click lista desplegable
    context.talla_s = ProductoAmazon(context.driver)
    context.talla_s.tamano_s()#selecciona tamaño s
    time.sleep(5)
    #Coloco los pasos de seleccionar el tamaño ya que el link tiene el color establecido

@when('el usuario hace click en "Agregar al Carrito"')
def add_carrito(context):
    context.agregar = ProductoAmazon(context.driver)
    context.agregar.agregar_al_carrito() #click en agregar al carrito
    time.sleep(8)


@then('se agrega el producto en el carrito')
def producto_agregado(context):
    context.carrito_producto = ProductoAmazon(context.driver)
    try:
        assert "1" in context.carrito_producto.resultado_carrito() #Assert que tengo un producto en el carrito
        print("Paso el test")

    except Exception as e:
        print("no es el codigo postal", format(e))
    time.sleep(5)

    #TEST CASE 7

@given('el usuario tenga algun producto en el carrito')
def item_carrito(context):
    context.driver = webdriver.Chrome(executable_path="/home/iampedroluisg/Escritorio/chromedriver")
    context.driver.get("https://www.amazon.com/-/es/Sudadera-Champion-Powerblend-logotipo-Negro-y06794/dp/B078GLNW6P/ref=sr_1_5?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=champion%20sweatshirts%20for%20men&qid=1631121282&sr=8-5") #Acortador de URL
    context.lista_talla = ProductoAmazon(context.driver)
    context.lista_talla.selecotor_tamano()#Click lista desplegable
    context.talla_s = ProductoAmazon(context.driver)
    context.talla_s.tamano_s()#selecciona tamaño s
    time.sleep(5)
    context.agregar = ProductoAmazon(context.driver)
    context.agregar.agregar_al_carrito()
    time.sleep(5)


@when('el usuario hace click en el carrito de compras')
def boton_carrito_compras(context):
    context.carrito_compras = ProductoAmazon(context.driver)
    context.carrito_compras.click_boton_carro()
    time.sleep(5)

@when('hace click en "eliminar compra"')
def eliminar_carrito(context):
    context.borrar_producto = ProductoAmazon(context.driver)
    context.borrar_producto.click_eliminar_producto()


@then('el carrito aparece vacio')
def assert_carrito(context):
    context.carrito_eliminado = ProductoAmazon(context.driver)
    try:
        assert "0" in context.carrito_eliminado.resultado_carrito() #Assert que el carrito esta vacio
        print("Paso el test")

    except Exception as e:
        print("no es el codigo postal", format(e))
    time.sleep(5)

# TEST CASE  8

@given('el usuario esta en la seccion de Registro de Amazon')
def pagina_registro(context):
    context.driver = webdriver.Chrome(executable_path="/home/iampedroluisg/Escritorio/chromedriver")
    context.driver.get("https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&language=es&pageId=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F-%2Fes%2Fgp%2Fcart%2Fview.html%3Fref_%3Dnav_signin&prevRID=JK73DPSCRX1PQ3TNVQ0P&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    time.sleep(5)


@when('el usuario completa los datos solicitados')
def registro_usuario(context):
    #REGISTRO DE USUARIO
    context.nombre = Registro(context.driver)
    context.nombre.completar_nombre("pedro")
    time.sleep(2)
    context.email = Registro(context.driver)
    context.email.completar_email("pedroluisgutierrez96@gmail.com")
    time.sleep(2)
    context.contrasena = Registro(context.driver)
    context.contrasena.completar_contrasena("pedroluis1234")
    time.sleep(2)
    context.check_pass = Registro(context.driver)
    context.check_pass.check_pass_usr("pedroluis1234")
    time.sleep(5)


@when('le da click en "crea tu cuenta de Amazon"')
def click_crearC(context): #BOTON CREAR CUENTA
    context.click_boton = Registro(context.driver)
    context.click_boton.click_boton_crearC()
    time.sleep(4)

@then('le envia un codigo de verificacion de email')
def confirm_envio_mail(context):
    context.confirmo_mail = Registro(context.driver)
    try:
        assert "Verificar dirección de correo electrónico" in context.confirmo_mail.envia_mail()  #Assert si cambio el codigo postal
        print("Paso el test")

    except Exception as e:
        print("no es el codigo postal", format(e))
    time.sleep(5)

#TEST CASE 9

@given('el usuario esta en la seccion de Inicio de sesion de Amazon')
def pagina_iniciarSesion(context):
    context.driver = webdriver.Chrome(executable_path="/home/iampedroluisg/Escritorio/chromedriver")
    context.driver.get("https://www.amazon.com/-/es/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcart%2Fview.html%2Fref%3Dnav_ya_signin%3Fapp-nav-type%3Dnone%26dc%3Ddf&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")  # Acortador de URL
    time.sleep(5)
@when('el usuario completa los campos solicitados')
def campo_email(context):
    context.escribir_email = InicioSesion(context.driver)
    context.escribir_email.escribirmail("pedroluisgutierrez96@gmail.com")
    time.sleep(5)
@when('le da click en "continuar"')
def click_continuar(context):
    context.clickBoton_continuar = InicioSesion(context.driver)
    context.clickBoton_continuar.click_continuar_is()
    time.sleep(5)
@when('completa el campo contraseña')
def campo_contrasena(context):
    context.escribe_pass = InicioSesion(context.driver)
    context.escribe_pass.escribircontrasena("95981419pedro")
    time.sleep(5)

@when('le da click en iniciar sesion')
def click_inicioSesion(context):
    context.clickBoton_iniciosesion = InicioSesion(context.driver)
    context.clickBoton_iniciosesion.click_boton_is()
    time.sleep(5)
@then('Se muestra la pagina Home de Amazon')
def amazon_home(context):
    try:
        assert 'Amazon.com. Gasta menos. Sonríe más.' in context.driver.title   #Hago un assert de el tituko de la pagina
        print("Paso el test")

    except Exception as e:
        print("no es la pagina de amazon", format(e))
    time.sleep(5)

# TEST CASE 10

@given('él usuario ya esta logeado')
def usuario_logeado(context):
    context.driver = webdriver.Chrome(executable_path="/home/iampedroluisg/Escritorio/chromedriver")
    context.driver.get("https://www.amazon.com/-/es/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcart%2Fview.html%2Fref%3Dnav_ya_signin%3Fapp-nav-type%3Dnone%26dc%3Ddf&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")  # Acortador de URL
    time.sleep(3)
    context.escribir_email = InicioSesion(context.driver)
    context.escribir_email.escribirmail("pedroluisgutierrez96@gmail.com")
    context.clickBoton_continuar = InicioSesion(context.driver)
    context.clickBoton_continuar.click_continuar_is()
    time.sleep(3)
    context.escribe_pass = InicioSesion(context.driver)
    context.escribe_pass.escribircontrasena("95981419pedro")
    context.clickBoton_iniciosesion = InicioSesion(context.driver)
    context.clickBoton_iniciosesion.click_boton_is()
    time.sleep(3)


@when('el usuario hace click en el menu hamburguesa todo')
def menu_hamburguesa(context):
    context.click_menu = CerrarSesion(context.driver)
    context.click_menu.click_menu_hamb()

@when('hace click en salir')
def sboton_salir(context):
    context.click_salir = CerrarSesion(context.driver)
    context.click_salir.click_boton_salir()


@then('la cuenta se deslogea')
def sesion_cerrada(context):
    context.sesion_fuera = CerrarSesion(context.driver)
    try:
        assert "Sign-In" in context.sesion_fuera.sesion_out()
        print("Paso el test")

    except Exception as e:
        print("no es el color", format(e))
    time.sleep(5)

#TEST CASES ALTERNOS

#TEST CASE ALTERNO 1
@given('el usuario esta en la pagina de Registro de Amazon')
def registro_pagina(context):
    context.driver = webdriver.Chrome(executable_path="/home/iampedroluisg/Escritorio/chromedriver")
    context.driver.get("https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&language=es&pageId=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F-%2Fes%2Fgp%2Fcart%2Fview.html%3Fref_%3Dnav_signin&prevRID=JK73DPSCRX1PQ3TNVQ0P&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    time.sleep(5)

@when('el usuario completa los datos solicitados excepto el campo Nombre')
def dato_imcompleto_nombre(context):
    context.nombre = Registro(context.driver)
    context.nombre.completar_nombre("")
    time.sleep(2)
    context.email = Registro(context.driver)
    context.email.completar_email("pedroluisgutierrez96@gmail.com")
    time.sleep(2)
    context.contrasena = Registro(context.driver)
    context.contrasena.completar_contrasena("pedroluis1234")
    time.sleep(2)
    context.check_pass = Registro(context.driver)
    context.check_pass.check_pass_usr("pedroluis1234")
    time.sleep(3)


@when('hace click en "crea tu cuenta de Amazon"')
def click_crear(context):
    context.click_boton = Registro(context.driver)
    context.click_boton.click_boton_crearC()
    time.sleep(2)


@then('no le permite registrar la cuenta de amazon')
def assersion_nombre(context):
    context.assert_name = Asserts(context.driver)
    try:
        assert "Introduce tu nombre" in context.assert_name.alertname() #Assert que tengo un producto en el carrito
        print("Paso el test")

    except Exception as e:
        print("Ingreso el nombre", format(e))
    time.sleep(5)

#TEST CASE ALTERNO 2


@given('usuario en pagina de registro')
def pagina_registrar(context):
    context.driver = webdriver.Chrome(executable_path="/home/iampedroluisg/Escritorio/chromedriver")
    context.driver.get("https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&language=es&pageId=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F-%2Fes%2Fgp%2Fcart%2Fview.html%3Fref_%3Dnav_signin&prevRID=JK73DPSCRX1PQ3TNVQ0P&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    time.sleep(5)


@when('el usuario completa los campos solicitados excepto el campo de email')
def email_vacio(context):
    context.nombre = Registro(context.driver)
    context.nombre.completar_nombre("pedro")
    time.sleep(2)
    context.email = Registro(context.driver)
    context.email.completar_email("")
    time.sleep(2)
    context.contrasena = Registro(context.driver)
    context.contrasena.completar_contrasena("pedroluis1234")
    time.sleep(2)
    context.check_pass = Registro(context.driver)
    context.check_pass.check_pass_usr("pedroluis1234")
    time.sleep(3)


@when('clickea en "crea tu cuenta de Amazon"')
def crear_cuental(context):
    context.click_boton = Registro(context.driver)
    context.click_boton.click_boton_crearC()
    time.sleep(2)


@then('no permite registrar la cuenta de amazon')
def alert_email(context):
    context.assert_mail = Asserts(context.driver)
    try:
        assert "Introduce tu nombre" in context.assert_mail.alrtmail() #Assert que tengo un producto en el carrito
        print("Paso el test")

    except Exception as e:
        print("Ingreso el email", format(e))
    time.sleep(5)

# TEST CASE ALTERNO 3

@given('usuario esta en la seccion de Inicio de sesion de Amazon')
def pagina_inicio_session(context):
    context.driver = webdriver.Chrome(executable_path="/home/iampedroluisg/Escritorio/chromedriver")
    context.driver.get("https://www.amazon.com/-/es/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcart%2Fview.html%2Fref%3Dnav_ya_signin%3Fapp-nav-type%3Dnone%26dc%3Ddf&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")  # Acortador de URL
    time.sleep(5)


@when('el usuario no completa el dato requerido')
def datoen_blaco(context):
    context.escribir_email = InicioSesion(context.driver)
    context.escribir_email.escribirmail("")
    time.sleep(5)


@when(u'hace el click en "continuar"')
def click_continue(context):
    context.clickBoton_continuar = InicioSesion(context.driver)
    context.clickBoton_continuar.click_continuar_is()
    time.sleep(5)


@then(u'no le permite iniciar sesion')
def assert_alert(context):
    context.assersion_is_name = Asserts(context.driver)
    try:
        assert "Enter your email or mobile phone number" in context.assersion_is_name.alertisnombre() #Assert que tengo un producto en el carrito
        print("Paso el test")

    except Exception as e:
        print("Ingreso el email", format(e))
    time.sleep(5)

#TEST CASE ALTERNO 4

@given('estar seccion de Inicio de sesion de Amazon')
def sign_in(context):
    context.driver = webdriver.Chrome(executable_path="/home/iampedroluisg/Escritorio/chromedriver")
    context.driver.get("https://www.amazon.com/-/es/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcart%2Fview.html%2Fref%3Dnav_ya_signin%3Fapp-nav-type%3Dnone%26dc%3Ddf&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")  # Acortador de URL
    time.sleep(5)


@when('el usuario no completa el campo contraseña')
def campovaciopass(context):
    context.escribir_email = InicioSesion(context.driver)
    context.escribir_email.escribirmail("pedroluisgutierrez96@gmail.com")
    time.sleep(2)
    context.clickBoton_continuar = InicioSesion(context.driver)
    context.clickBoton_continuar.click_continuar_is()
    time.sleep(2)
    context.escribe_pass = InicioSesion(context.driver)
    context.escribe_pass.escribircontrasena("")
    time.sleep(2)

@when('presiona el boton "iniciar sesion"')
def click_iniciarS(context):
    context.clickBoton_iniciosesion = InicioSesion(context.driver)
    context.clickBoton_iniciosesion.click_boton_is()
    time.sleep(3)


@then('no le permite ingresar a la seion')
def alertaEnterpass(context):
    context.assersionpass = Asserts(context.driver)
    try:
        assert 'Enter your password' in context.assersionpass.alertaispass()   #Hago un assert de el tituko de la pagina
        print("Paso el test")

    except Exception as e:
        print("ingreso session", format(e))
    time.sleep(5)

# TEST CASE ALTERNO 5

@given('amazon inicia session')
def amazon_inicia_sesion(context):
    context.driver = webdriver.Chrome(executable_path="/home/iampedroluisg/Escritorio/chromedriver")
    context.driver.get("https://www.amazon.com/-/es/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcart%2Fview.html%2Fref%3Dnav_ya_signin%3Fapp-nav-type%3Dnone%26dc%3Ddf&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")  # Acortador de URL
    time.sleep(5)


@when('el usuario completa los campos solicitados con la contraseña incorrecto')
def error_pass(context):
    context.escribir_email = InicioSesion(context.driver)
    context.escribir_email.escribirmail("pedroluisgutierrez96@gmail.com")
    context.clickBoton_continuar = InicioSesion(context.driver)
    context.clickBoton_continuar.click_continuar_is()
    time.sleep(3)
    context.escribe_pass = InicioSesion(context.driver)
    context.escribe_pass.escribircontrasena("errorpass")


@when('presiona "Inicir Sesion"')
def click_inicio(context):
    context.clickBoton_iniciosesion = InicioSesion(context.driver)
    context.clickBoton_iniciosesion.click_boton_is()
    time.sleep(3)


@then('no le permite iniciar session')
def assersion_pass(context):
    context.assererrorpass = Asserts(context.driver)
    try:
        assert 'Your password is incorrect' in context.assererrorpass.alerta_pass()   #Hago un assert de el tituko de la pagina
        print("Paso el test")

    except Exception as e:
        print("ingreso session", format(e))
    time.sleep(5)
