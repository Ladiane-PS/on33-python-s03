# Crie um programa onde a usuária deve inseri8r uma nota de 1 a 10 e imprime se a aluna foi a provada ou reprovada, a nota mínima para aprovação é 7. 
# também é necessário que a aluna tenha uma frequência de 75% para ser aprovada

# codigo feito em grupo 

# # Solicita a nota da aluna
nota = float(input('Digite a nota da aluna (de 1 a 10): '))

# # Solicita a frequência da aluna
frequencia = float(input('Digite a frequência da aluna (em %): '))

# # Verifica se a aluna foi aprovada
if nota >= 7 and frequencia >= 75:
     print('Aluna aprovada!')
else:

     print('Aluna reprovada.')





# Solicita a nota da aluna e verifica se está dentro do intervalo válido (1 a 10)


# nota = float(input("Insira a nota da aluna (de 1 a 10): "))
# while nota < 1 or nota > 10:
#     print("Nota inválida. Por favor, insira uma nota entre 1 e 10.")
#     nota = float(input("Insira a nota da aluna (de 1 a 10): "))

# # Solicita a frequência da aluna e verifica se está dentro do intervalo válido (0 a 100)
# frequencia = float(input("Insira a frequência da aluna (0 a 100): "))
# while frequencia < 0 or frequencia > 100:
#     print("Frequência inválida. Por favor, insira uma frequência entre 0 e 100.")
#     frequencia = float(input("Insira a frequência da aluna (0 a 100): "))

# # Verifica se a aluna foi aprovada ou reprovada
# if nota >= 7 and frequencia >= 75:
#     print(f"A aluna foi aprovada com nota {nota:.2f} e frequência {frequencia:.2f}%.")
# else:
#     print(f"A aluna foi reprovada com nota {nota:.2f} e frequência {frequencia:.2f}%.")

