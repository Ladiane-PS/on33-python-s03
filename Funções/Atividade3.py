# Atividade 3
#Crie uma função que converte uma temperatura de graus Celsius para Fahrenheit. Use try e except para garantir que a entrada seja um número
def celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32
entrada = input("Digite a temperatura em graus Celsius: ")
try:
    celsius = float(entrada)
    fahrenhet = celsius_para_fahrenheit(celsius)
    print(f"A temperatura de {celsius} °C corresponde a {fahrenhet } °F")
except:
    print("Erro, digite um número válido")
                                                        