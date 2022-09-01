from PyPDF2 import PdfFileReader


pdf_name = "RAD_Python_Aula_01.pdf"

pdf_arquivo = open("RAD em Python/aula05/RAD_Python_Aula_01.pdf", "rb")

pdf_content = PdfFileReader(pdf_arquivo)

pdf_information = pdf_content.getDocumentInfo()
pdf_numpage = pdf_content.getNumPages()

page_1 = pdf_content.getPage(1)

texto = f"""
Informação sobre {pdf_name}

Autor: {pdf_information.author}
Criador: {pdf_information.creator}
Título: {pdf_information.title}
Assunto: {pdf_information.subject}
Número de páginas: {pdf_numpage}
Conteúdo da Página 1: {page_1.extractText()}"""

print(texto)


pdf_arquivo.close()