filmes=["up as altas aventuras","chainsaw main arc da reze","kimetsu no yaiba castelo ifinito "]
for filme in filmes:
    nome=input("digite nome de um filme ou clica f para sair:")

    filmes.append(nome)
    if nome == "f " or nome == "F":
        break
print(filmes)   
