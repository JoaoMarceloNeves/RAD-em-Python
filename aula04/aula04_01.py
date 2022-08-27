# Manipulação de Strings
#   - excelente site para aprender várias coisas sobre python:
#       https://www.w3schools.com/python/

arquivo = open("RAD em Python/aula04/teste04_01.txt", "r")

print("Representação após o strip")
for linha in arquivo:
    linha_limpa = linha.strip()
    print(repr(linha_limpa))

arquivo.close()