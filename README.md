# Organizador de Arquivos por Tipo

Este é um script Python simples que organiza os arquivos de um diretório de acordo com o tipo de arquivo.

## Como Usar

1. Clone este repositório ou baixe o arquivo `organizador_de_arquivos.py`.
2. Certifique-se de ter o Python instalado em seu sistema.
3. Execute o script Python `organizador_de_arquivos.py`.
4. Uma janela de seleção de diretório será aberta. Escolha o diretório que deseja organizar e clique em "Selecionar Pasta".
5. O script irá analisar o diretório selecionado e moverá os arquivos para subpastas de acordo com o tipo de arquivo.

## Estrutura de Pasta Após a Execução

O script irá criar as seguintes subpastas no diretório selecionado e moverá os arquivos correspondentes para cada uma delas:

- **imagens**: Para arquivos de imagem (`.png`, `.jpg`, `.jpeg`, `.webp`).
- **PDFs**: Para arquivos PDF (`.pdf`).
- **Excel**: Para arquivos Excel (`.xlsx`).
- **SVG**: Para arquivos SVG (`.svg`).
- **ZIP**: Para arquivos ZIP (`.zip`).
- **MP4**: Para arquivos de vídeo (`.mp4`, `.mkv`).
- **MP3**: Para arquivos de áudio (`.mp3`).
- **Executáveis**: Para arquivos executáveis (`.exe`).

Certifique-se de revisar as pastas após a execução do script para garantir que os arquivos foram organizados corretamente.

## Pré-requisitos

- Python 3.x

## Observações

- Certifique-se de que o Python está corretamente instalado e configurado em seu sistema antes de executar o script.
- Este script moverá os arquivos para subpastas no diretório selecionado. Certifique-se de selecionar um diretório adequado para organizar os arquivos.
- Os arquivos serão movidos de acordo com sua extensão. Se desejar adicionar mais tipos de arquivos a serem organizados, você pode editar o dicionário `locais` no script.

---

# Combinar arquivos PDF usando PyPDF2

Este script Python demonstra como combinar vários arquivos PDF em um único arquivo usando a biblioteca PyPDF2.

## Pré-requisitos

Certifique-se de ter Python e a biblioteca PyPDF2 instalados em seu ambiente de desenvolvimento. Você pode instalar o PyPDF2 usando o seguinte comando:

```bash
pip install PyPDF2
