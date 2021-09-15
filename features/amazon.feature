@feature
Feature: Pagina web de amazon
  "Como usuario quiero tener una pagina web para comprar productos online"
  @tchp1
  Scenario: TC1 Ingresar a la pagina web de amazon.com.
    Given Tener acceso a internet
    When  el usuario busca en google amazon
    And   ingresa en el link de amazon
    Then  puede ver la home de amazon

  @tchp2
  Scenario: TC2 Busqueda de producto
    Given Tener acceso a la pagina de amazon
    When  el escribe busca sudaderas de hombre champion en la barra de busqueda
    And   hace click en el boton buscar
    Then  se visualizan los resultados del producto buscado

  @tchp3
  Scenario: TC3 Cambiar color al producto
    Given haber seleccionado un producto
    When  el usuario selecciona otro color disponible
    Then  Se visualiza el mismo producto con otro color


  @tchp4
  Scenario: TC4 Cambiar tamaño del producto
    Given haber seleccionado un producto
    When  el usuario hace click en la lista desplegable de "Tamaño"
    And   selecciona el tamaño deseado
    Then  se visualiza el producto con el talle deseado

  @tchp5
  Scenario: TC5 Agregar Codigo Postal de Miami
    Given que el usuario este en el Home de Amazon
    When  el usuario hace click en "Enviar a"
    And   escribe el Codigo Postal de Miami que es 33101
    And   hace click en "aplicar"
    And   hace click en "continuar"
    Then  Se visualiza el cambio de locacion

  @tchp6
  Scenario: TC6 Agregar al carrito de compras
    Given que el usuario haya seleccionado el producto deseado
    When  el usuario hace click en "Agregar al Carrito"
    Then  se agrega el producto en el carrito

  @tchp7
  Scenario: TC7 Eliminar compra
    Given el usuario tenga algun producto en el carrito
    When  el usuario hace click en el carrito de compras
    And   hace click en "eliminar compra"
    Then  el carrito aparece vacio

  @tchp8
  Scenario: TC8 Registrarse
    Given el usuario esta en la seccion de Registro de Amazon
    When  el usuario completa los datos solicitados
    And   le da click en "crea tu cuenta de Amazon"
    Then  le envia un codigo de verificacion de email

  @tchp9
  Scenario: TC9 Inicio sesion
    Given el usuario esta en la seccion de Inicio de sesion de Amazon
    When  el usuario completa los campos solicitados
    And   le da click en "continuar"
    And   completa el campo contraseña
    And   le da click en iniciar sesion
    Then  Se muestra la pagina Home de Amazon

  @tchp10
  Scenario: TC10 Cerrar sesion
    Given él usuario ya esta logeado
    When  el usuario hace click en el menu hamburguesa todo
    And   hace click en salir
    Then  la cuenta se deslogea


    #TESTCASE ALTERNOS

  @tcalt1
  Scenario: TCALT1 Registro Sin Campo Nombre
    Given el usuario esta en la pagina de Registro de Amazon
    When  el usuario completa los datos solicitados excepto el campo Nombre
    And   hace click en "crea tu cuenta de Amazon"
    Then  no le permite registrar la cuenta de amazon

  @tcalt2
  Scenario: TCALT2 Registro Sin Campo email
    Given usuario en pagina de registro
    When  el usuario completa los campos solicitados excepto el campo de email
    And   clickea en "crea tu cuenta de Amazon"
    Then  no permite registrar la cuenta de amazon

  @tcalt3
  Scenario: TCALT3 Inicio sesion email vacio
    Given usuario esta en la seccion de Inicio de sesion de Amazon
    When  el usuario no completa el dato requerido
    And   hace el click en "continuar"
    Then  no le permite iniciar sesion

  @tcalt4
  Scenario: TCALT4 Inicio sesion contraseña vacio
    Given estar seccion de Inicio de sesion de Amazon
    When  el usuario no completa el campo contraseña
    And   presiona el boton "iniciar sesion"
    Then  no le permite ingresar a la seion

  @tcalt5
  Scenario: TCALT5 Contraseña incorrecta
    Given amazon inicia session
    When  el usuario completa los campos solicitados con la contraseña incorrecto
    And   presiona "Inicir Sesion"
    Then  no le permite iniciar session


