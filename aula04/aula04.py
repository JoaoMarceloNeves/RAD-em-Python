# Manipulação de Strings
#   - excelente site para aprender várias coisas sobre python:
#       https://www.w3schools.com/python/


#   Lembra que vem o \n quando lemos o conteúdo de um arquivo? E se a gente quiser tirar esse \n?

arquivo = open("RAD em Python/aula04/teste04_01.txt", "r")

print("Representação original da linha: ")
for linha in arquivo:
    print(repr(linha))

arquivo.close()