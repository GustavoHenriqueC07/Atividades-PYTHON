nota1 = int(input("Qual a nota da sua primeira prova?"))
nota2 = int(input("Qual a nota do seu trabalho?"))
nota3 = int(input("Qual a nota da sua segunda prova?"))

resultado = nota1 + nota2 + nota3
media = resultado / 3

if media >= 7:
    print("Parabéns! Você passou de ano!")

elif media >= 5:
    print("Você está de recuperação")

else:
    print("Você reprovou")