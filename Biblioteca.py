opcao = 0
estante = []
print("========== Biblioteca da Brubs ==========")

menu = """
 MENU:
 1) Todos os livros
 2) Adicionar um novo livro
 3) Buscar livro pelo autor
 4) Remover livro pelo código
 5) Quantidade de livros no sistema
 6) Sair do sistema
 """

while opcao != 6:
    print(menu)
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        if len(estante) > 0:
            print("\n===== LISTA DE LIVROS =====")
            for i in range(len(estante)):
                print(f"{i + 1} - {estante[i][0]} ({estante[i][1]})")
        else:
            print("\n[ERRO] Nenhum livro encontrado!")

    elif opcao == 2:
        while True:
            novo_livro = input("\nDigite o nome do novo livro: ")
            autor_livro = input("Digite o nome do autor: ")
            estante.append([novo_livro, autor_livro])
            print(f"- {novo_livro} de {autor_livro} foi adicionado com sucesso!")
            continuar = input("\nGostaria de adicionar mais um livro? (S/N): ").upper()
            if continuar == "N":
                break

    elif opcao == 3:
        if estante:
            autor_buscado = input("\nDigite o nome do autor que deseja buscar: ")
            print(f"\nLivros encontrados de {autor_buscado}:")

            livros_encontrados = []
            for livro, autor in estante:
                if autor_buscado.lower() in autor.lower():
                    livros_encontrados.append(livro)

            if livros_encontrados:
                for i, livro in enumerate(livros_encontrados, 1):
                    print(f"{i} - {livro}")
            else:
                print("[ERRO] Nenhum livro desse autor foi cadastrado.")
        else:
            print("\n[ERRO] Nenhum livro na estante para buscar.")

    elif opcao == 4:
        if estante:
            codigo_livro = int(input("\nDigite o código do livro que deseja remover: "))
            if 1 <= codigo_livro <= len(estante):
                livro_removido = estante.pop(codigo_livro - 1)
                print(f"O livro '{livro_removido[0]}' foi removido com sucesso!")
        else:
            print("\n[ERRO] Nenhum livro cadastrado para remover.")

    elif opcao == 5:
        print(f"Quantidade de livros cadastrados na estante: {len(estante)}")
        
    elif opcao == 6:
        print("\nObrigado por usar o programa da Biblioteca da Brubs!")
        
    else:
        print("\n[ERRO] Opção Inválida, tente novamente.")