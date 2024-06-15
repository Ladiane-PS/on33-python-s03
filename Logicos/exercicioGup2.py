# Solicita a nota da aluna
nota = float(input('Digite a nota da aluna (de 1 a 10): '))

# Solicita a frequência da aluna
frequencia = float(input('Digite a frequência da aluna (em %): '))

# Verifica se a aluna foi aprovada
if nota >= 7 and frequencia >= 75:
    print('Aluna aprovada!')
else:
    print('Aluna reprovada.')
