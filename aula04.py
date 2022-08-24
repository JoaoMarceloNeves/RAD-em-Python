# Manipulação de Strings

#   Lembra que vem o \n quando lemos o conteúdo de um arquivo? E se a gente quiser tirar esse \n?

#arquivo = open("RAD em Python/teste04_01.txt", "r")

# 1 -----------------------------------------------
#print("Representação original da linha: ")
#for linha in arquivo:
#    print(repr(linha))

# 2 -----------------------------------------------
#print("Representação após o strip")
#for linha in arquivo:
#    linha_limpa = linha.strip()
#    print(repr(linha_limpa))

# 3 -----------------------------------------------
# O método strip() pode ser usada para saber quantas linhas um arquivo tem (descontando as linhas em branco)
#contador = 0
#contador_2 = 0
#for linha in arquivo:
#    if linha:
#        contador += 1
#    if linha.strip():
#        contador_2 += 1

#print("Total = ", contador)
#print("Total real = ", contador_2)

#--------------------------------------------------
#arquivo.close()

#
# excelente site para aprender várias coisas sobre python:
#   https://www.w3schools.com/python/
#
# 4 -----------------------------------------------
# Método count
#frase = "As pessoas precisam saber, saber, que até mesmo o sanduiche iche, tem propriedades nutritivas"
#contador = frase.count("saber")
#print("Total de vezes da palavra 'saber': ", contador)

#contardor2 = frase.count("iche")
#print("Quantidade de vezes da palavra 'iche': ", contardor2)

# 5 -----------------------------------------------
# Método split()
#frase = "uma frase de teste para vermos o método"
#lista_frase = frase.split(' ')
#print(lista_frase)

# 6 -----------------------------------------------
# Método join()
#lista_string = ['C', 'Lua', 'Java']

#texto1 = ', '.join(lista_string)
#print(texto1)

#texto2 = '\n'.join(lista_string)
#print(texto2)

# 7 -----------------------------------------------
# Formatação de Strings
#   - f-strings
#   - format()
#   - manualmente

# 7.1 ----------------------------------------------
# f-strings
# 7.1.1 --------------------------------------------
#nome = "Fulano"
#teste_string = "Olá " + nome + "."
#teste_fstring1 = f"Olá {nome}."
#teste_fstring2 = f"Olá {nome.upper()}."
#teste_fstring3 = f"Quantos anos você tem? {pow(2,5)}."
#teste_fstring4 = f"O número 2 é maior que 1? {2>1}"
#teste_fstring5 = f"O número 5 está na lista [1, 2, 3, 4]? {5 in [1, 2, 3, 4]}"

#print(teste_string)
#print(teste_fstring1)
#print(teste_fstring2)
#print(teste_fstring3)
#print(teste_fstring4)
#print(teste_fstring5)

# 7.1.2 --------------------------------------------
#from cmath import pi
#from datetime import datetime

#frutas = ["Pera", "Uca", "Maçã", "Sala Mista"]
#for fruta in frutas:
#    fruta_string = f"Nome: {fruta:12} - Número de letras: {len(fruta): 3}"
#    print(fruta_string)

#print() # apenas para dar uma quebra de linha

#pi_string = f"O número pi é: {pi:.1f}"
#pi_string2 = f"O número pi deslocado é: {pi:6.1f}"
#pi_string3 = f"O número pi com 4 casas decimais: {pi:.4f}"
#print(pi_string)
#print(pi_string2)
#print(pi_string3)

#print() # apenas para dar uma quebra de linha

#data = datetime.now()
#data_string = f"A data de hoje é {data}"
#data_string2 = f"A data de hoje formatada: {data: %d/%m/%y}"
#print(data_string)
#print(data_string2)

# 7.2 ----------------------------------------------
# format()
#teste_string = "O valor é {preco:.2f} reais"
#print(teste_string.format(preco = 39.99))

#teste_string2 = "Olá! Meu nome é {nome}, e eu tenho {idade} anos".format(nome = "Evandro", idade = 20)
#teste_string3 = "Olá! Meu nome é {0}, e eu tenho {1} anos".format("Evandro", 20)
#teste_string4 = "Olá! Meu nome é {}, e eu tenho {} anos".format("Evandro", 20)

#print(teste_string2)
#print(teste_string3)
#print(teste_string4)