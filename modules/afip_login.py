"""Functions for logging into AFIP."""
from selenium.webdriver.common.by import By
from utils.selenium_helpers import wait_for_element

def login_afip(driver, cuil, password):
    """Log into AFIP with the given credentials."""
    print("✍️  INGRESANDO CUIL")
    usuario_input = driver.find_element(By.ID, "F1:username")
    usuario_input.send_keys(cuil)
    
    boton_siguiente = driver.find_element(By.ID, "F1:btnSiguiente")
    boton_siguiente.click()
    
    print("⌛ CORROBORANDO CUIL")
    try:
        wait_for_element(driver, By.ID, "F1:password")
        print("✅ CUIL ACEPTADO")
    except Exception as e:
        print(f"Error en la validación del CUIL: {e}")
        return False
    
    print("✍️  INGRESANDO CONTRASEÑA")
    pass_input = driver.find_element(By.ID, "F1:password")
    pass_input.send_keys(password)
    
    boton_ingresar = driver.find_element(By.ID, "F1:btnIngresar")
    boton_ingresar.click()
    
    print("⌛ CORROBORANDO CONTRASEÑA")
    try:
        wait_for_element(
            driver, 
            By.XPATH, 
            "//h3[@class='roboto-font regular p-y-0 m-y-0 h4'][text()='Comprobantes en línea']",
            clickable=True
        )
        print("✅ CONTRASEÑA ACEPTADA")
        return True
    except Exception as e:
        print(f"Error en la validación de la contraseña: {e}")
        return False
