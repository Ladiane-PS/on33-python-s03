# ERRO DE TIPO (TYPEERROR)
# Erros de tipo ocorrem quando você tenta realizar uma operação em um tipo de dado
# que não é compatível com essa operação

# a = " string" + 5
# print("O resultado é: " , a) # errado

a = "string" + str (5) 
print("O resultado é : ", a) # correto
