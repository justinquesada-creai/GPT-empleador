# GPT-empleador

## 📊 Integración con Google Sheets usando Python

Este proyecto demuestra cómo interactuar con Google Sheets mediante Python usando la librería `gspread` y autenticación con Service Account.

## ✨ Características

- ✅ Autenticación segura con Google Service Account
- 📖 Lectura de celdas individuales
- ✏️ Escritura de datos en celdas
- 📊 Obtención de todas las filas de una hoja
- 🔒 Protección de credenciales con `.gitignore`

## 🚀 Inicio Rápido

Para instrucciones detalladas de instalación y configuración, consulta [README_SETUP.md](README_SETUP.md)

```bash
# 1. Instalar dependencias
pip install gspread google-auth

# 2. Configurar credentials.json (ver README_SETUP.md)

# 3. Ejecutar el script
python test.py
```

## 📁 Estructura del Proyecto

- `test.py` - Script principal de prueba
- `credentials.json` - Archivo de credenciales (NO incluido en Git)
- `README_SETUP.md` - Guía detallada de configuración