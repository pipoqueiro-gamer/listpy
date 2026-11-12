from datetime import datetime

livros = []

while True:
  continuacao = input(
      "Quer cadastrar um livro? Digite 's' para sim ou 'n' para não: "
  )

  if continuacao == "n" or continuacao == "N":
    break

  nome = input("Escreva o nome de um livro: ")
  titulo = input("Escreva o título: ")
  autor = input("Escreva o nome do autor: ")

  # Recebe a data do usuário e converte com datetime
  data_texto = input("Escreva a data de publicação (DD/MM/AAAA): ")
  ano = datetime.strptime(data_texto, "%d/%m/%Y").date()

  # Usa colchetes [ ] dentro do append para agrupar os 4 itens em um único livro
  livros.append([nome, ano, titulo, autor])

  print("\nLista atual de livros:")
  for livro in livros:
    # livro[1] é a data; usamos strftime para mostrar no padrão brasileiro
    data_bonita = livro[1].strftime("%d/%m/%Y")
    print(
        f"Nome: {livro[0]} | Data: {data_bonita} | Título: {livro[2]} | Autor:"
        f" {livro[3]}"
    )
  print("-" * 30)

  

    
