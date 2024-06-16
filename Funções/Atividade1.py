# Crie uma função que soma dois números fornecidos pelos usuário.
# Use o try e except para garantir que as entradas sejam números e 
# exiba o resultado da soma 


def soma (a,b):
    return a + b
entrada1 = input("Digite o primeiro número:")
entrada2 = input("Digite o segundo número:")

try:
    numero1 = float(entrada1)
    numero2 = float(entrada2)
    resultado = soma(numero1, numero2)
    print(f"A soma do {numero1} e {numero2} é {resultado}")
except:
    print(f"Entrada inválida")

# Relembrando Funções

# uma função é um bloco de código reutilizável que realiza uma tarefa
# específica, Funções ajudam a organizar e estruturae o código, tornando-o 
# mais legíveis e fácil de manter. Em python, uma função e definida usando a palavra-chave
# def seguida pelo nome da função, parênteses e dois pontos.

# funções internas
#  O Python possui várias funções internas (built-in functions) que estão prontas
# para serem usasadas sem necessidade de importação ou definição prévia.
# print() exibi uma mensagem na tela
# len() Retorna o comprimento(número de elementos) de um objeto
# input() Recebe uma entrada do usu´srio
# int() Converte uma string ou número para um inteiro 
# float()Converte uma string ou número para um ponto flutuante