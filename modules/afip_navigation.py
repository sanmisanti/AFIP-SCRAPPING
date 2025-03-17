"""Functions for navigating within AFIP."""
from selenium.webdriver.common.by import By
import time
from config.config import CREDENTIALS
from utils.selenium_helpers import wait_for_element, set_input_value_js

def navigate_to_ver_todos(driver):
    try:
        link = driver.find_element(By.XPATH, '//a[contains(@class, "roboto-font") and contains(@class, "h4") and (text()="Ver todos")]')
        link.click()
        return True
    except Exception as e:
        print(f"Error al seleccionar ver todos: {e}")
        return False
    
    

def navigate_to_mis_comprobantes(driver):
    """Navigate to the 'Comprobantes en línea' section."""
    element = driver.find_element(By.XPATH, '//h3[contains(text(), "MIS COMPROBANTES")]')
    print("element: ", element)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(1)
    element.click()
    
    print("⌛ TU PUTA VIEJA")
    time.sleep(3)  # Wait for the new window to open
    
    # Switch to the new window
    ventana_original = driver.window_handles[0]
    ventanas = driver.window_handles

    print("ventanas; ", ventanas)
    
    for ventana in ventanas:
        if ventana != ventana_original:
            driver.switch_to.window(ventana)
            break
    
    print("🪟  bien puta")
    return True
    
def navigate_to_persona(driver):
    try:
        # Agarra los primeros dos numeros despues un guion y despues antes del ultimo utro guion
        cuil = CREDENTIALS["cuil"]
        formated_cuil = cuil[:2] + "-" + cuil[2:-1] + "-" + cuil[-1]

        link = driver.find_element(By.XPATH,  f'//small[text()="{formated_cuil}"]')
        link.click()
        return True
    except Exception as e:
        print(f"Error al seleccionar ver todos: {e}")
        return False
    
def navigate_to_emitidos(driver):
    try:
        element = driver.find_element(By.XPATH, '//h3[contains(text(), "Emitidos")]')
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        return True
    except Exception as e:
        print(f"Error al seleccionar ver todos: {e}")
        return False
    
def navigate_to_recibidos(driver):
    try:
        element = driver.find_element(By.XPATH, '//h3[contains(text(), "Recibidos")]')
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        element.click()
        return True
    except Exception as e:
        print(f"Error al seleccionar ver todos: {e}")
        return False
    
# 14/03/2024 - 14/03/2025

def set_date(driver, fecha_desde, fecha_hasta):
    """Set search parameters."""
    try:
        fd_input = wait_for_element(
            driver, 
            By.ID, 
            "fechaEmision",
            clickable=True
        )
        fecha = f"{fecha_desde} - {fecha_hasta}"
        print("fecha: ", fecha)
        set_input_value_js(driver, fd_input, fecha)
        return True
    except Exception as e:
        print(f"Error al configurar parámetros de búsqueda: {e}")
        return False
    
def search_mis_comprobantes(driver):
    """Execute the search for comprobantes."""
    print("🔍 BUSCANDO COMPROBANTES")
    try:
        buscar = wait_for_element(
            driver, 
            By.ID, 
            "buscarComprobantes",
            clickable=True
        )
        buscar.click()
        time.sleep(3)
        # Wait for search results to load
        wait_for_element(
            driver, 
            By.XPATH, 
            '//tr[contains(@class, "odd")]',
            clickable=True
        )
        return True
    except Exception as e:
        print(f"Error al buscar comprobantes: {e}")
        return False
    
def change_cantidad_de_registros(driver):
    """Execute the search for comprobantes."""
    print("🔍 CANTIDAD DE REGISTROS")
    try:
        select = wait_for_element(
            driver, 
            By.XPATH, 
            "//button[@title='Cantidad de registros por página']",
            clickable=True
        )
        select.click()
        
        # Wait for search results to load
        cantidad = driver.find_element(By.XPATH, '//a[contains(text(), "50")]')
        cantidad.click()
        return True
    except Exception as e:
        print(f"Error al registros: {e}")
        return False

def navigate_to_comprobantes(driver):
    """Navigate to the 'Comprobantes en línea' section."""
    comprobantes_element = driver.find_element(
        By.XPATH, 
        "//h3[@class='roboto-font regular p-y-0 m-y-0 h4'][text()='Comprobantes en línea']"
    )
    comprobantes_element.click()
    
    print("⌛ ABRIENDO VENTANA")
    time.sleep(3)  # Wait for the new window to open
    
    # Switch to the new window
    ventana_original = driver.window_handles[0]
    ventanas = driver.window_handles
    
    for ventana in ventanas:
        if ventana != ventana_original:
            driver.switch_to.window(ventana)
            break
    
    print("🪟  VENTANA ABIERTA")
    return True

def select_user_profile(driver):
    """Select the user profile."""
    try:
        boton = wait_for_element(
            driver, 
            By.XPATH, 
            "//input[@type='button'][@value='SAN MIGUEL SANTIAGO']",
            clickable=True
        )
        boton.click()
        return True
    except Exception as e:
        print(f"Error al seleccionar el perfil de usuario: {e}")
        return False
    


def navigate_to_consultas(driver):
    """Navigate to the 'Consultas' section."""
    try:
        boton = wait_for_element(
            driver, 
            By.XPATH, 
            "//span[text()='Consultas']",
            clickable=True
        )
        boton.click()
        return True
    except Exception as e:
        print(f"Error al navegar a Consultas: {e}")
        return False

def set_search_parameters(driver, fecha_desde):
    """Set search parameters."""
    try:
        fd_input = wait_for_element(
            driver, 
            By.NAME, 
            "fechaEmisionDesde",
            clickable=True
        )
        set_input_value_js(driver, fd_input, fecha_desde)
        return True
    except Exception as e:
        print(f"Error al configurar parámetros de búsqueda: {e}")
        return False

def search_comprobantes(driver):
    """Execute the search for comprobantes."""
    print("🔍 BUSCANDO COMPROBANTES")
    try:
        buscar = wait_for_element(
            driver, 
            By.XPATH, 
            "//input[@value='Buscar']",
            clickable=True
        )
        buscar.click()
        
        # Wait for search results to load
        wait_for_element(
            driver, 
            By.XPATH, 
            "//td[@title='Fecha de Emisión']",
            clickable=True
        )
        return True
    except Exception as e:
        print(f"Error al buscar comprobantes: {e}")
        return False