# Manipulação de Strings
#   - excelente site para aprender várias coisas sobre python:
#       https://www.w3schools.com/python/

arquivo = open("RAD em Python/aula04/teste04_01.txt", "r")

# O método strip() pode ser usada para saber quantas linhas um arquivo tem (descontando as linhas em branco)
contador = 0
contador_2 = 0
for linha in arquivo:
    if linha:
        contador += 1
    if linha.strip():
        contador_2 += 1

print("Total = ", contador)
print("Total real = ", contador_2)

arquivo.close()