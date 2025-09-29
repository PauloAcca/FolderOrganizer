import os

from pathlib import Path

carpeta_objetivo = Path.home() / "Downloads" | Path.home() / "Descargas"

categorias = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "Musica": [".mp3", ".wav", ".flac", ".aac"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
}

categoria_predeterminada = ["Otros"]

extension_a_categoria = {}

for categoria, extensiones in categorias.items():
    for extension in extensiones:
        extension_a_categoria[extension.lower()] = categoria

archivos = [f for f in carpeta_objetivo.iterdir() if f.is_file()]

for archivo in archivos:
    ext = archivo.suffix.lower()
    categoria = extension_a_categoria.get(ext, categoria_predeterminada[0])
    destino_dir = carpeta_objetivo / categoria
    destino_dir.mkdir(exist_ok=True)
    if not (destino_dir / archivo.name).exists():
        archivo.rename(destino_dir / archivo.name)
        print(f"Movido {archivo.name} a {categoria}")
    else:
        i = 1
        while (destino_dir / (archivo.name + "(" + str(i) + ")")).exists():
            i += 1
        archivo.rename(destino_dir / (archivo.name + "(" + str(i) + ")"))
        print(f"Movido {archivo.name} a {categoria} con nombre {archivo.name}({i})")