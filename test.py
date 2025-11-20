import gspread
from google.oauth2.service_account import Credentials

# 1. Configuración
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CREDENTIALS_FILE = 'credentials.json'
SPREADSHEET_ID = '15rGBlTF-qrjROL71vErROttOOcH5nnnhwAeLJWNSH-w'  # ✅ Solo el ID

def main():
    print(" Autenticando con Service Account...")
    
    # 2. Autenticar
    creds = Credentials.from_service_account_file(
        CREDENTIALS_FILE,
        scopes=SCOPES
    )
    client = gspread.authorize(creds)
    
    print(" Autenticación exitosa!")
    
    # 3. Abrir el Sheet
    print(f"\n Abriendo Google Sheet con ID: {SPREADSHEET_ID}")
    sheet = client.open_by_key(SPREADSHEET_ID).sheet1
    
    print(" Sheet abierto correctamente!")
    
    # 4. LEER - Obtener valor de celda A1
    print("\n LEYENDO celda A1...")
    valor_a1 = sheet.acell('A1').value
    print(f"   Valor en A1: '{valor_a1}'")
    
    # 5. ESCRIBIR - Escribir en celda C1
    print("\n  ESCRIBIENDO en celda C1...")
    sheet.update_acell('C1', '¡Hola Mundo desde Python!')
    print("   Escritura exitosa!")
    
    # 6. LEER - Verificar que se escribió
    print("\n Verificando celda C1...")
    valor_c1 = sheet.acell('C1').value
    print(f"   Valor en C1: '{valor_c1}'")
    
    # 7. LEER - Obtener todas las filas
    print("\n Leyendo todas las filas...")
    all_values = sheet.get_all_values()
    print(f"   Total de filas: {len(all_values)}")
    
    if all_values:
        print("\n   Primeras 3 filas:")
        for i, row in enumerate(all_values[:3], 1):
            print(f"   {i}. {row}")
    
    print("\n🎉 ¡Test completado exitosamente!")

if __name__ == "__main__":
    main()
