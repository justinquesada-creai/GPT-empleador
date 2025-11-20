# 📋 Setup - Google Sheets con Python

Este proyecto permite leer y escribir datos en Google Sheets usando Python y gspread.

## 🔧 Instalación

```bash
pip install gspread google-auth
```

## 🔑 Configuración de Credenciales

### 1. Crear una Cuenta de Servicio en Google Cloud

1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Crea un nuevo proyecto o selecciona uno existente
3. Habilita la **Google Sheets API**
4. Ve a **IAM & Admin** > **Service Accounts**
5. Crea una nueva cuenta de servicio
6. Descarga el archivo JSON de credenciales

### 2. Configurar el archivo credentials.json

Copia el archivo JSON descargado y renómbralo como `credentials.json` en la raíz del proyecto.

El archivo debe tener esta estructura:

```json
{
  "type": "service_account",
  "project_id": "tu-proyecto-id",
  "private_key_id": "...",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "tu-service-account@tu-proyecto.iam.gserviceaccount.com",
  "client_id": "...",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "..."
}
```

### 3. Compartir tu Google Sheet

**IMPORTANTE:** Comparte tu Google Sheet con el email de la cuenta de servicio (se encuentra en el campo `client_email` del JSON).

## ▶️ Uso

```bash
python test.py
```

## ⚠️ Seguridad

- **NUNCA** subas el archivo `credentials.json` a Git
- Este archivo contiene credenciales sensibles
- Ya está incluido en `.gitignore` para protección

