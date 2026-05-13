from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.add_argument('--start-maximized') #Opcional, ventana maximizada
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(5) #Espera implicita profesional

try:
    # 1)Login

    driver.get("https://saucedemo.com") #Ingresa a la pagina de prueba
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]' ).click()

    # 2) Validar que estamos en inventario

    assert '/inventory.html' in driver.current_url
    print('Test Ok')

    # 3) Verificar titulo de seccion
    
    titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == 'Products'
    print('Titulo de seccion OK ->', titulo)

    # 4) Contar productos visibles

    productos = driver.find_elements(By.CSS_SELECTOR, 'div.inventory_item')
    print(f'Se encontraron {len(productos)} productos.')
    assert len(productos) > 0
    # 5) Añadir el primer producto al carrito

    productos[0].find_element(By.TAG_NAME, 'button').click()
    producto0 = productos[0].find_element(By.CSS_SELECTOR, 'div.inventory_item_name').text
    producto0 = productos[0].find_element(By.CSS_SELECTOR, 'div.inventory_item_name').text
    precio0 = productos[0].find_element(By.CSS_SELECTOR, 'div.inventory_item_price').text
    print(f'Nombre: {producto0}, Precio: {precio0}')

    # 6) Confirmar que el badge del carrito muestra 1

    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert badge == '1'
    print('Carrito OK ->', badge)

    driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
    time.sleep(5)
    assert '/cart.html' in driver.current_url

    item_carrito = driver.find_element(By.CSS_SELECTOR, '.inventory_item_name').text
    assert item_carrito == producto0
    print('Producto en la lista OK ->', item_carrito)
    
finally:
    driver.quit()   #Cierre limpio. Mata la sesion y la ventana