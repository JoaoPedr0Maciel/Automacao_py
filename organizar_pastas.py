import os
from tkinter.filedialog import askdirectory

caminho = askdirectory() 
print(caminho)

lista_de_arquivos = os.listdir(caminho)

locais = {
  "imagens": [".png", ".jpg", ".jpeg", ".webp"],
  "PDFs": [".pdf"],
  "Excel": [".docx"],
  "SVG": [".svg"],
  "ZIP": [".zip"],
  "MP4": [".mp4", ".mkv"],
  "MP3": [".mp3"],
  "Executaveis": [".exe"],
    
}

for arquivo in lista_de_arquivos:
  nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
  for pasta in locais:
    if extensao in locais[pasta]:
      if not os.path.exists(f"{caminho}/{pasta}"):
        os.mkdir(f"{caminho}/{pasta}")
      os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")