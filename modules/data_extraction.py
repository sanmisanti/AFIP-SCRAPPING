"""Functions for extracting data from AFIP."""
from selenium.webdriver.common.by import By
import openpyxl

def extract_table_data(driver):
    """Extract data from the results table."""
    print("📝 EXTRAYENDO DATOS")
    try:
        tabla = driver.find_element(By.CLASS_NAME, "jig_table")
        tbody = tabla.find_element(By.TAG_NAME, "tbody")
        filas = tbody.find_elements(By.TAG_NAME, "tr")
        
        # Extract data from the table
        datos = [[celda.text for celda in fila.find_elements(By.TAG_NAME, "td")] for fila in filas]
        
        # Remove empty rows
        datos = [fila for fila in datos if fila]
        return datos
    except Exception as e:
        print(f"Error al extraer datos de la tabla: {e}")
        return []

def save_to_excel(datos, filename):
    """Save data to an Excel file."""
    print("📝 GENERANDO EXCEL")
    try:
        libro = openpyxl.Workbook()
        hoja = libro.active
        
        # Write data to Excel
        for fila_idx, fila in enumerate(datos, start=1):
            for col_idx, valor in enumerate(fila, start=1):
                hoja.cell(row=fila_idx, column=col_idx, value=valor)
        
        # Save Excel file
        libro.save(filename)
        print("🎉 EXCEL LISTO!!")
        return True
    except Exception as e:
        print(f"Error al guardar el archivo Excel: {e}")
        return False