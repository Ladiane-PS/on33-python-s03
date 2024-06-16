# Atividfade 4
# Crie uma função que conta o número de caracteres em uma string fornecida 
# pelo usuário. Use try e except para garantir que a entrda seja uma string 

def contarCaracteres(texto):
    return len(texto)
entrada = input ("Digite uma palavra ou uma frase:")

try:
    caracteres = contarCaracteres(entrada)
    print(f"A string{entrada}, têm {caracteres} caracteres")
except:
    print("Erro, digite uma palabvra ou frase")    