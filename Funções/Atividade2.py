# Atividade 2
# Crie uma função que verifica se um número é par ou ímpar. Use try e except para garantir que a entrada seja um número. 

def parImpar (numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
entrada = input("Digite um número inteiro:")

try:
    numero = int(entrada)
    resultado = parImpar(numero)
    print(f"O número {numero} é {resultado}")
except:
    print(f"Erro: Digite um número inteiro")