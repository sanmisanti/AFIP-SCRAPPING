"""Functions for navigating within AFIP."""
from selenium.webdriver.common.by import By
import time
from utils.selenium_helpers import wait_for_element, set_input_value_js

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