quantidade = int(input("Quantos nomes você quer cadastrar? "))

nomes = []

for i in range(quantidade):
    nome = input("Digite um nome: ")

    nomes.append(nome)

print(nomes)