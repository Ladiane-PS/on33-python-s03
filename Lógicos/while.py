while True:
    nota = int(input(" Insira uma nota de 1 a 10: "))
    if 1 <= nota <= 10:  # Verifica se a nota está dentro do intervalo válido (entre 1 e 10)
        if nota >= 7:
            print("Aprovada")
        else:
            print("Reprovada")
        break  # Sai do loop quando a nota válida é inserida e o resultado é impresso