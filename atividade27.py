# Solicite ao usuário que insira o nome de até 7 convidados.
# Armazene os nomes em uma lista.
# Permita ao usuário remover um convidado da lista, caso necessário.
# Exiba a lista final de convidados.

# Digite o nome do convidado 1: João
# Digite o nome do convidado 2: Maria
# ...
# Digite o nome do convidado 7: Pedro
# Deseja remover algum convidado da lista? (sim/não): sim
# Digite o nome do convidado a ser removido: Maria

n = str("uff")
l = []

for no in range(7):
    x = input(f"Digite o nome do {no + 1}° convidado:   ")
    l.append(x)

    if no == 6:
        r = input("Remover algum convidado da lista? Responda com Sim ou Não.   ")

if r == "Sim" or r == "S" or r == "s" or r == "sim":
    re = input("Qual convidado deseja remover?   ")
    l.remove(re)
    print(f"Sua lista de convidados é:   {l}")

else:
    print(f"Sua lista de convidados é:   {l}")