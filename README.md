# 📂 Folder Organizer

Este proyecto es un **script en Python** que organiza automáticamente los archivos de tu carpeta de **Descargas/Downloads** en subcarpetas según su tipo (imágenes, videos, documentos, música, etc.).

## 🚀 Características
- Detecta automáticamente si tu carpeta se llama **Downloads** o **Descargas**.
- Clasifica los archivos por categorías:
  - Imágenes (`.jpg`, `.png`, `.gif`, etc.)
  - Videos (`.mp4`, `.avi`, `.mkv`, etc.)
  - Música (`.mp3`, `.wav`, `.flac`, etc.)
  - Documentos (`.pdf`, `.docx`, `.xlsx`, etc.)
  - Comprimidos (`.zip`, `.rar`, `.7z`, etc.)
- Los archivos que no encajan en ninguna categoría se mueven a la carpeta **Otros**.
- Si un archivo con el mismo nombre ya existe, el script agrega un número al final para evitar sobrescribirlo.

---

## 📋 Requisitos
- Python **3.8+**
- Funciona en **Windows, Linux y macOS**
- No requiere instalar librerías externas (usa solo librerías estándar de Python).

---

## 🔧 Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/PauloAcca/FolderOrganizer.git
   cd FolderOrganizer

## ▶️ Uso
  1.	Abrí una terminal en la carpeta del proyecto.
	2.	Ejecutá el script: python organizer.py (asumiendo que guardaste el código en un archivo llamado organizer.py)
  3.	El script moverá los archivos de tu carpeta Descargas/Downloads a las carpetas correspondientes:
  	•	Imagenes/
  	•	Videos/
  	•	Musica/
  	•	Documentos/
  	•	Comprimidos/
  	•	Otros/

## 📝 Ejemplo de salida
  Movido foto1.jpg a Imagenes
  Movido informe.pdf a Documentos
  Movido video.mp4 a Videos
  Movido archivo.zip a Comprimidos

## ⚠️ Notas
	•	Este script mueve los archivos, no los copia.
	•	Si querés probarlo sin arriesgar tus archivos, podés crear una carpeta de prueba con algunos archivos de ejemplo y cambiar la       variable carpeta_objetivo en el código.

## Extra

Podes modificarlo para que organize en mas carpeteas y tipos de archivos, este fue armado para uso propio.
