# Tratamento de exceções durante a manipulação de arquivos

#   "Ao desenvolver um programa, precisamos procurar na documentação da biblioteca, do módulo ou 
# da própria linguagem de programação se as funcionalidades que vamos utilizar têm exceções mape
# adas. Essas exceções são problemas que podem ocorrer, e é nossa tarefa tratá-las."
#
#   "Tratar uma exceção nada mais é do que dizer ao Python o que fazer, ou quais instruções exe
# cutar, quando ele encontrar um problema."

# 1 -----------------------------------------------------
# Arquivo não existe
#arquivo = open("RAD em Python/aula05/teste01.txt", "r")
# Exceção FileNotFoundError é lançada e a execução é interrompida. O que fazer para que a execu
# ção não seja interrompida?

#print("Arquivo abrido")

# 2 -----------------------------------------------------
try:
    arquivo = open("RAD em Python/aula05/teste01.txt", "r")
    print("Arquivo abrido")
#except Exception as erro:
except FileNotFoundError as erro:
    print("Arquivo não pôde ser abrido")
    print("Descrição: ", erro)
    
# Outras exceções para vocês testarem:
#   - FileExistsError
#   - IsADirectoryError (dica: tente remover uma pasta usando os.remove)

# Exercício:
#   - Atualizar todo o código que vocês vieram fazendo até então, acrescentando try-except para lidar com exceções
#   - Utilizar outros métodos providos pelo Python, tanto para arquivos, como para pastas (exemplo: rename)