numero = 5
if numero % 2 == 0: 
    print ('O número é Par')
else:
    print ('O número é Impar') 



# if É uma declaração condicional em Python que permite executar um bloco de código se uma condição for verdadeira.
# numero É uma variável que contém um valor numérico (um número inteiro, por exemplo).
# % É o operador de módulo em Python. Ele retorna o resto da divisão entre dois números.
# É o divisor. Aqui estamos verificando se o numero é divisível por 2.
# == É o operador de igualdade em Python. Ele compara dois valores e retorna True se forem iguais e False se forem diferentes.
# É o valor com o qual estamos comparando o resultado da operação numero % 2.

# Explicação do Funcionamento:
# A operação numero % 2 calcula o resto da divisão de numero por 2.
# Se numero é um número par, o resto dessa divisão será 0.
# Se numero é um número ímpar, o resto dessa divisão será 1.
# Exemplo Prático:
# Se numero for 4:

# 4 % 2 resulta em 0 (porque 4 dividido por 2 dá 2, com resto 0).
# Então, 4 % 2 == 0 será True, e o bloco de código dentro do if será executado.
# Se numero for 5:

# 5 % 2 resulta em 1 (porque 5 dividido por 2 dá 2, com resto 1).
# Então, 5 % 2 == 0 será False, e o bloco de código dentro do if não será executado.
