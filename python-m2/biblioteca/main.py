from typing import List
from livros import (
    Livro,
    cadastrar_livro,
    buscar_por_titulo,
    buscar_por_autor,
)
from usuarios import (
    Usuario,
    cadastrar_usuario,
    buscar_usuario_por_cpf,
)
from emprestimos import (
    emprestar_livro,
    devolver_livro,
    listar_emprestimos_usuario,
)
from persistencia import carregar_tudo, salvar_tudo


def menu() -> str:
    """
    Exibe o menu principal e retorna a opção escolhida pelo usuário.

    Returns:
        str: opção escolhida pelo usuário.
    """
    print("\n=== SISTEMA DE BIBLIOTECA ===")
    print("1. Cadastrar livro")
    print("2. Cadastrar usuário")
    print("3. Realizar empréstimo")
    print("4. Devolver livro")
    print("5. Consultar livros")
    print("6. Listar empréstimos de um usuário")
    print("7. Sair e salvar")
    return input("Escolha uma opção: ")


def main() -> None:
    """
    Função principal do sistema da biblioteca.

    Responsável por:
    - carregar os dados salvos em JSON,
    - exibir o menu interativo,
    - gerenciar as operações (cadastro, consulta, empréstimo e devolução),
    - salvar os dados ao encerrar.
    """
    print("Carregando dados...")
    acervo, usuarios, emprestimos = carregar_tudo()
    print("Dados carregados com sucesso!\n")

    while True:
        opcao = menu()

        # cad livro
        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano de publicação: "))
            exemplares = int(input("Número de exemplares: "))
            cadastrar_livro(acervo, titulo, autor, ano, exemplares)
            print("Livro cadastrado com sucesso!")

        # 2 cad usuario
        elif opcao == "2":
            nome = input("Nome do usuário: ")
            cpf = input("CPF: ")
            try:
                cadastrar_usuario(usuarios, nome, cpf)
                print("Usuário cadastrado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        # emprestimo
        elif opcao == "3":
            cpf = input("CPF do usuário: ")
            usuario = buscar_usuario_por_cpf(usuarios, cpf)
            if not usuario:
                print("Usuário não encontrado.")
                continue
            titulo = input("Título do livro: ")
            livros_encontrados = buscar_por_titulo(acervo, titulo)
            if not livros_encontrados:
                print("Livro não encontrado.")
                continue
            livro = livros_encontrados[0]
            try:
                emprestar_livro(usuario, livro, emprestimos)
                print("Empréstimo realizado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        # devolv livro
        elif opcao == "4":
            cpf = input("CPF do usuário: ")
            usuario = buscar_usuario_por_cpf(usuarios, cpf)
            if not usuario:
                print("Usuário não encontrado.")
                continue
            titulo = input("Título do livro a devolver: ")
            livros_encontrados = buscar_por_titulo(acervo, titulo)
            if not livros_encontrados:
                print("Livro não encontrado.")
                continue
            livro = livros_encontrados[0]
            try:
                devolver_livro(usuario, livro, emprestimos)
                print("Livro devolvido com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        # opcoes livros
        elif opcao == "5":
            tipo = input("Buscar por (T)título ou (A)autor? ").strip().lower()
            termo = input("Digite o termo de busca: ")
            if tipo == "t":
                encontrados = buscar_por_titulo(acervo, termo)
            else:
                encontrados = buscar_por_autor(acervo, termo)
            if encontrados:
                print("\n--- LIVROS ENCONTRADOS ---")
                for l in encontrados:
                    print(f"{l.titulo} ({l.autor}, {l.ano}) - {l.exemplares} exemplares disponíveis")
            else:
                print("Nenhum livro encontrado.")

        # emprestimo do usuario
        elif opcao == "6":
            cpf = input("CPF do usuário: ")
            usuario = buscar_usuario_por_cpf(usuarios, cpf)
            if not usuario:
                print("Usuário não encontrado.")
                continue
            emprestimos_usuario = listar_emprestimos_usuario(usuario, emprestimos)
            if emprestimos_usuario:
                print("\n--- EMPRÉSTIMOS ATIVOS ---")
                for e in emprestimos_usuario:
                    print(f"Livro: {e.livro.titulo}")
            else:
                print("Nenhum empréstimo ativo.")

        # sair
        elif opcao == "7":
            print("Salvando dados...")
            salvar_tudo(acervo, usuarios, emprestimos)
            print("Dados salvos com sucesso. Encerrando o sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
