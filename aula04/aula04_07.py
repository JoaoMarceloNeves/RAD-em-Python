# Manipulação de Strings
#   - excelente site para aprender várias coisas sobre python:
#       https://www.w3schools.com/python/


# Formatação de Strings
#   - f-strings
#   - format()
#   - manualmente

# Aula 04.07 ---------------------------------------
# format()
teste_string = "O valor é {preco:.2f} reais"
print(teste_string.format(preco = 39.99))

teste_string2 = "Olá! Meu nome é {nome}, e eu tenho {idade} anos".format(nome = "Evandro", idade = 20)
teste_string3 = "Olá! Meu nome é {0}, e eu tenho {1} anos".format("Evandro", 20)
teste_string4 = "Olá! Meu nome é {}, e eu tenho {} anos".format("Evandro", 20)

print(teste_string2)
print(teste_string3)
print(teste_string4)