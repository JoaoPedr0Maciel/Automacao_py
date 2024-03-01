# Combinar arquivos PDF usando PyPDF2

Este script Python demonstra como combinar vários arquivos PDF em um único arquivo usando a biblioteca PyPDF2.

## Pré-requisitos

Certifique-se de ter Python e a biblioteca PyPDF2 instalados em seu ambiente de desenvolvimento. Você pode instalar o PyPDF2 usando o seguinte comando:

```bash
pip install PyPDF2

## Uso

1. Clone este repositório ou baixe o arquivo `combine_pdfs.py`.
2. Crie uma pasta chamada `arquivos` no mesmo diretório onde o script `combine_pdfs.py` está localizado.
3. Coloque todos os arquivos PDF que deseja combinar na pasta `arquivos`.
4. Execute o script Python `combine_pdfs.py`.

O script lerá todos os arquivos PDF na pasta `arquivos`, os combinará em um único arquivo PDF e salvará o resultado como `PDF Final.pdf` no mesmo diretório.

Certifique-se de que todos os arquivos PDF que deseja combinar estão na pasta `arquivos` antes de executar o script. Os arquivos serão combinados na ordem alfabética dos nomes dos arquivos.
