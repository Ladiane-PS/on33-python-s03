# ATIVIDADE
# Crie um programa onde a usuária deve inserir uma nota de 1 a 10 e imprimir se a aluna foi aprovada ou reprovada, a nota mínima para a aprovação é 7.

# codigo feito em grupo 
nota = float(input("Insira a nota da aluna (de 1 a 10): "))


# # Verifica se a nota é válida (entre 1 e 10)
if nota < 1 or nota > 10:
     print("Nota inválida. Por favor, insira uma nota entre 1 e 10.")
else:
#     # Verifica se a nota é suficiente para aprovação
   if nota >= 7:
         print(f"A aluna foi aprovada com nota {nota:.2f}.")
   else:
         print(f"A aluna foi reprovada com nota {nota:.2f}.")   

   # .2f:
# .2: Especifica que queremos duas casas decimais.
#f: Indica que o número deve ser formatado como um ponto flutuante (float).


# # @@ para retornar e inserir denovo o processo
# nota = float(input("Insira a nota da aluna (de 1 a 10): "))

# # Verifica se a nota é válida (entre 1 e 10)
# while nota < 1 or nota > 10:
#     print("Nota inválida. Por favor, insira uma nota entre 1 e 10.")
#     nota = float(input("Insira a nota da aluna (de 1 a 10): "))

# # Verifica se a nota é suficiente para aprovação
# if nota >= 7:
#     print(f"A aluna foi aprovada com nota {nota:.2f}.")
# else:
#     print(f"A aluna foi reprovada com nota {nota:.2f}.")   

# # O processo se repete enquanto a expressão booleana continuar sendo verdadeira.
# # Quando a expressão se torna falsa, a execução do while é interrompida e o controle passa para o próximo bloco de código após o while.




