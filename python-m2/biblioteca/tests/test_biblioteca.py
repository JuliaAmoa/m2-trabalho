import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from livros import cadastrar_livro, buscar_por_titulo
from usuarios import cadastrar_usuario, buscar_usuario_por_cpf
from emprestimos import emprestar_livro, devolver_livro, listar_emprestimos_usuario


def testar_cadastro_e_busca() -> None:
    """
    Testa o cadastro e a busca de livros no acervo.
    """
    print("\n=== Teste: Cadastro e busca de livros ===")
    acervo = []
    cadastrar_livro(acervo, "Dom Casmurro", "Machado de Assis", 1899, 3)
    cadastrar_livro(acervo, "O Alienista", "Machado de Assis", 1882, 2)
    resultado = buscar_por_titulo(acervo, "dom")
    for livro in resultado:
        print(f"Encontrado: {livro.titulo} ({livro.exemplares} exemplares)")


def testar_usuarios() -> None:
    """
    Testa o cadastro e busca de usuários da biblioteca.
    """
    print("\n=== Teste: Cadastro e busca de usuários ===")
    usuarios = []
    cadastrar_usuario(usuarios, "Maria", "123")
    cadastrar_usuario(usuarios, "João", "456")
    usuario = buscar_usuario_por_cpf(usuarios, "123")
    print(f"Usuário encontrado: {usuario.nome} - CPF {usuario.cpf}")


def testar_emprestimo_e_devolucao() -> None:
    """
    Testa o fluxo completo de empréstimo e devolução de livros.
    """
    print("\n=== Teste: Empréstimo e devolução ===")
    from livros import Livro
    from usuarios import Usuario

    livro = Livro("Dom Casmurro", "Machado de Assis", 1899, 1)
    usuario = Usuario("Maria", "123")
    emprestimos = []

    # Empréstimo
    emprestar_livro(usuario, livro, emprestimos)
    print(f"Livro emprestado! Exemplares restantes: {livro.exemplares}")

    # Listar empréstimos do usuário
    ativos = listar_emprestimos_usuario(usuario, emprestimos)
    for e in ativos:
        print(f"Empréstimo ativo: {e.livro.titulo}")

    # Devolução
    devolver_livro(usuario, livro, emprestimos)
    print(f"Livro devolvido! Exemplares disponíveis: {livro.exemplares}")


def main() -> None:
    """
    Executa todos os testes manuais de forma sequencial.
    """
    testar_cadastro_e_busca()
    testar_usuarios()
    testar_emprestimo_e_devolucao()
    print("\n Todos os testes manuais foram executados com sucesso.")


if __name__ == "__main__":
    main()
