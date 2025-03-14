from modules.afip_navigation import (
    navigate_to_comprobantes, 
    select_user_profile, 
    navigate_to_consultas,
    set_search_parameters,
    search_comprobantes
)
from modules.data_extraction import extract_table_data
from config.constants import AFIP_LOGIN_URL
from utils.selenium_helpers import initialize_driver
from modules.afip_login import login_afip

def getData(cuil, password, fecha_desde):
    driver = initialize_driver(headless=True)
    
    try:
        # Open login page
        driver.get(AFIP_LOGIN_URL)
        
        # Login
        login_successful = login_afip(driver, cuil, password)
        if not login_successful:
            print("Error en el inicio de sesión. Abortando...")
            return
        
        # Navigate to Comprobantes en línea
        navigate_to_comprobantes(driver)
        
        # Select user profile
        if not select_user_profile(driver):
            print("Error al seleccionar el perfil. Abortando...")
            return
        
        # Navigate to Consultas
        if not navigate_to_consultas(driver):
            print("Error al navegar a Consultas. Abortando...")
            return
        
        # Set search parameters
        if not set_search_parameters(driver, fecha_desde):
            print("Error al configurar parámetros de búsqueda. Abortando...")
            return
        
        # Search for comprobantes
        if not search_comprobantes(driver):
            print("Error al buscar comprobantes. Abortando...")
            return
        
        # Extract data
        datos = extract_table_data(driver)
        if not datos:
            print("No se encontraron datos para extraer. Abortando...")
            return
        keys = ["fecha_emision", "tipo", "numero", "tipo_identificacion", "identificacion", "codigo", "monto", "campo1", "campo2", "campo3", "campo4"]        

        # Convertir la lista en una lista de diccionarios
        data_json = [dict(zip(keys, valores)) for valores in datos]
        print("data_json: ", data_json)
        return data_json
        
    finally:
        driver.quit()