# Atividade 5
# #Crie uma função que soma dois números fornecidos pelo usuário.Use o try
# e except para garantir que as entradas sejam números e exiba o resultado da soma
# Utilize if e else para verificar se a soma é positiva, negativa ou zero 
def somar_numeros():
    try:
        # Solicita os números do usuário
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        
        # Calcula a soma
        soma = numero1 + numero2
        
        # Verifica se a soma é positiva, negativa ou zero
        if soma > 0:
            print(f"A soma dos números é {soma:.2f} e é positiva.")
        elif soma < 0:
            print(f"A soma dos números é {soma:.2f} e é negativa.")
        else:
            print(f"A soma dos números é {soma:.2f} e é igual a zero.")
    
    except ValueError:
        # Tratamento de erro caso as entradas não sejam números
        print("Erro: Por favor, insira apenas números.")

# Chama a função para executar
somar_numeros()
   
   

# @@@@@@@@@@
# def soma_dois_numeros(a, b):
#     return a + b

# def main():
#     try:
#         num1 = float(input("Digite o primeiro número: "))
#         num2 = float(input("Digite o segundo número: "))
        
#         soma = soma_dois_numeros(num1, num2)
        
#         if soma > 0:
#             print(f"A soma é positiva: {soma}")
#         elif soma < 0:
#             print(f"A soma é negativa: {soma}")
#         else:
#             print(f"A soma é zero: {soma}")
    
#     except ValueError:
#         print("Erro: Por favor, insira apenas números.")
#     except Exception as e:
#         print(f"Ocorreu um erro inesperado: {e}")

# # Chama a função principal para executar o código
# main()   






