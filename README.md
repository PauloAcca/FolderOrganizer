## 📂 Folder Organizer

This project is a Python script that automatically organizes the files in your Downloads/Descargas folder into subfolders based on their type (images, videos, documents, music, etc.).

## 🚀 Features
	•	Automatically detects whether your folder is named Downloads or Descargas.
	•	Classifies files into categories:
	•	Images (.jpg, .png, .gif, etc.)
	•	Videos (.mp4, .avi, .mkv, etc.)
	•	Music (.mp3, .wav, .flac, etc.)
	•	Documents (.pdf, .docx, .xlsx, etc.)
	•	Archives (.zip, .rar, .7z, etc.)
	•	Files that don’t match any category are moved to the Others folder.
	•	If a file with the same name already exists, the script appends a number to avoid overwriting it.

⸻

## 📋 Requirements
	•	Python 3.8+
	•	Works on Windows, Linux, and macOS
	•	No need to install external libraries (uses only Python standard libraries).

⸻

## 🔧 Installation
	1.	Clone the repository:
git clone https://github.com/PauloAcca/FolderOrganizer.git
cd FolderOrganizer

⸻

## ▶️ Usage
	1.	Open a terminal in the project folder.
	2.	Run the script: python organizer.py (assuming you saved the code in a file called organizer.py)
	3.	The script will move the files from your Downloads/Descargas folder into the following folders:
• Imagenes/
• Videos/
• Musica/
• Documentos/
• Comprimidos/
• Otros/

⸻

## 📝 Example Output

Movido foto1.jpg a Imagenes
Movido informe.pdf a Documentos
Movido video.mp4 a Videos
Movido archivo.zip a Comprimidos

⸻

## ⚠️ Notes
	•	This script moves files, it does not copy them.
	•	If you want to test it safely, you can create a test folder with sample files and change the carpeta_objetivo variable in the code.

⸻

## 🛠️ Extra

You can customize it to organize into more folders, subfolders, or even target a different directory than Downloads, with different file types. This version was built for personal use.
