"""Main script to automate AFIP data extraction."""
from utils.selenium_helpers import initialize_driver
from modules.afip_login import login_afip
from modules.afip_navigation import (
    navigate_to_comprobantes, 
    select_user_profile, 
    navigate_to_consultas,
    set_search_parameters,
    search_comprobantes,
    navigate_to_ver_todos,
    navigate_to_mis_comprobantes,
    navigate_to_persona,
    navigate_to_emitidos,
    set_date,
    search_mis_comprobantes,
    change_cantidad_de_registros,
    navigate_to_recibidos
)
from selenium.webdriver.common.by import By
from modules.data_extraction import extract_table_data, save_to_excel, extract_table
from config.config import CREDENTIALS
from config.constants import AFIP_LOGIN_URL, SEARCH_DATE_FROM, OUTPUT_FILE
import time
from datetime import datetime
from datetime import timedelta

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
        
        
        
        if not navigate_to_ver_todos(driver):
            print("Error al ver todos. Abortando...")
            return
        
        time.sleep(3)
        
        
        if not navigate_to_mis_comprobantes(driver):
            print("Error al ver mis comptrobantes. Abortando...")
            return
        
        time.sleep(3)
        
        
        """ if not navigate_to_persona(driver):
            print("Error al entrar a la persona. Abortando...")
            return """
        
        fecha_hasta = datetime.today().date()
        fecha_desde = fecha_hasta - timedelta(days=360)

        fecha_hasta_str = fecha_hasta.strftime("%d/%m/%Y")
        fecha_desde_str = fecha_desde.strftime("%d/%m/%Y")
        
        for i in range(5):
            if not navigate_to_emitidos(driver):
                print("Error al entrar emitidos. Abortando...")
                return

            if not set_date(driver, fecha_desde_str, fecha_hasta_str):
                print("Error AL SET DATE. Abortando...")
                return

            time.sleep(3)

            if not search_mis_comprobantes(driver):
                print("Error AL SEARCH MIS COMPROBANTES. Abortando...")
                return
            
            if not change_cantidad_de_registros(driver):
                print("Error change_cantidad_de_registros. Abortando...")
                return
            
            time.sleep(3)

            datos = extract_table(driver)
            if not datos:
                print("No se encontraron datos para extraer. Abortando...")
                return

            # Save data to Excel
            save_to_excel(datos, "emitidos.xlsx")
            driver.back()

            fecha_hasta_str = fecha_desde_str
            fecha_desde_str = (fecha_desde - timedelta(days=319)).strftime("%d/%m/%Y")
            fecha_desde = fecha_desde - timedelta(days=319)

        fecha_hasta = datetime.today().date()
        fecha_desde = fecha_hasta - timedelta(days=360)

        fecha_hasta_str = fecha_hasta.strftime("%d/%m/%Y")
        fecha_desde_str = fecha_desde.strftime("%d/%m/%Y")

        for i in range(5):
            if not navigate_to_recibidos(driver):
                print("Error al entrar recibidos. Abortando...")
                return

            if not set_date(driver, fecha_desde_str, fecha_hasta_str):
                print("Error AL SET DATE. Abortando...")
                return

            time.sleep(3)

            if not search_mis_comprobantes(driver):
                print("Error AL SEARCH MIS COMPROBANTES. Abortando...")
                return
            
            if not change_cantidad_de_registros(driver):
                print("Error change_cantidad_de_registros. Abortando...")
                return
            
            time.sleep(3)

            datos = extract_table(driver)
            if not datos:
                print("No se encontraron datos para extraer. Abortando...")
                return

            # Save data to Excel
            save_to_excel(datos, "recibidos.xlsx")
            driver.back()

            fecha_hasta_str = fecha_desde_str
            fecha_desde_str = (fecha_desde - timedelta(days=319)).strftime("%d/%m/%Y")
            fecha_desde = fecha_desde - timedelta(days=319)
        
        """ # Localizar el botón de descarga (ajusta el selector según tu caso)
        boton_descarga = driver.find_element(By.XPATH, "//button[@title='Exportar como CSV']")  # Ajusta el XPATH

        # Hacer clic en el botón para descargar el archivo CSV
        boton_descarga.click()

        # Esperar a que la descarga se complete (puedes usar un tiempo de espera aquí también)
        time.sleep(5)  # Ajusta el tiempo según lo que tarde la descarga """
    
        
        """ datos = extract_table(driver)
        if not datos:
            print("No se encontraron datos para extraer. Abortando...")
            return
        
        # Save data to Excel
        save_to_excel(datos, OUTPUT_FILE) """
        
        
        
        """ # Navigate to Comprobantes en línea
        navigate_to_comprobantes(driver)
        
        # Select user profile
        if not select_user_profile(driver):
            print("Error al seleccionar el perfil. Abortando...")
            return """
        
        
        
        # Navigate to Consultas
        """ if not navigate_to_consultas(driver):
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
        save_to_excel(datos, OUTPUT_FILE) """
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()