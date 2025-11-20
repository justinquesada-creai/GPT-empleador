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
- `requirements.txt` - Dependencias del proyecto

## 🚀 Siguientes Pasos

### Integración con AWS Lambda

El siguiente paso en la evolución de este proyecto será desplegar la funcionalidad en **AWS Lambda**, lo que permitirá:

- ⚡ **Ejecución serverless**: Sin necesidad de mantener servidores activos
- 🔄 **Automatización**: Ejecutar el código en respuesta a eventos (cron jobs, API calls, etc.)
- 💰 **Costos reducidos**: Solo pagas por el tiempo de ejecución
- 🌐 **Escalabilidad**: AWS Lambda escala automáticamente según la demanda
- 🔗 **Integración con otros servicios AWS**: S3, DynamoDB, EventBridge, etc.

### Próximas características planeadas:

1. 📦 Crear función Lambda con capa para dependencias (`gspread`, `google-auth`)
2. 🔐 Almacenar credenciales de forma segura en AWS Secrets Manager o Parameter Store
3. ⏰ Configurar triggers automáticos con EventBridge (CloudWatch Events)
4. 🌐 Exponer funcionalidad mediante API Gateway
5. 📊 Implementar logging y monitoreo con CloudWatch