"""Main script to automate AFIP data extraction."""
from utils.selenium_helpers import initialize_driver
from modules.afip_login import login_afip
from modules.afip_navigation import (
    navigate_to_comprobantes, 
    select_user_profile, 
    navigate_to_consultas,
    set_search_parameters,
    search_comprobantes
)
from modules.data_extraction import extract_table_data, save_to_excel
from config.config import CREDENTIALS
from config.constants import AFIP_LOGIN_URL, SEARCH_DATE_FROM, OUTPUT_FILE

def main():
    """Main function to run the AFIP automation."""
    driver = initialize_driver(headless=True)
    
    try:
        # Open login page
        driver.get(AFIP_LOGIN_URL)
        
        # Login
        login_successful = login_afip(driver, CREDENTIALS["cuil"], CREDENTIALS["password"])
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
        if not set_search_parameters(driver, SEARCH_DATE_FROM):
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
        
        # Save data to Excel
        save_to_excel(datos, OUTPUT_FILE)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()