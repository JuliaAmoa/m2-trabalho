from typing import List, Dict
from livros import Livro
from usuarios import Usuario


class Emprestimo:
    """Representa um empréstimo de livro."""

    def __init__(self, usuario: Usuario, livro: Livro):
        self.usuario = usuario
        self.livro = livro

    def to_dict(self) -> Dict:
        return {
            "usuario_cpf": self.usuario.cpf,
            "livro_titulo": self.livro.titulo,
        }

    @staticmethod
    def from_dict(d: Dict, usuarios: List[Usuario], livros: List[Livro]) -> 'Emprestimo':
        usuario = next((u for u in usuarios if u.cpf == d["usuario_cpf"]), None)
        livro = next((l for l in livros if l.titulo == d["livro_titulo"]), None)
        if not usuario or not livro:
            raise ValueError("Erro ao carregar empréstimo: usuário ou livro inexistente.")
        return Emprestimo(usuario, livro)


def emprestar_livro(usuario: Usuario, livro: Livro, emprestimos: List[Emprestimo]) -> Emprestimo:
    """Registra o empréstimo de um livro, se houver exemplares disponíveis."""
    if livro.exemplares <= 0:
        raise ValueError("Não há exemplares disponíveis para empréstimo.")
    livro.exemplares -= 1
    novo = Emprestimo(usuario, livro)
    emprestimos.append(novo)
    return novo


def devolver_livro(usuario: Usuario, livro: Livro, emprestimos: List[Emprestimo]) -> None:
    """Devolve um livro emprestado, se o empréstimo existir."""
    for e in emprestimos:
        if e.usuario.cpf == usuario.cpf and e.livro.titulo == livro.titulo:
            emprestimos.remove(e)
            livro.exemplares += 1
            return
    raise ValueError("Empréstimo não encontrado para devolução.")


def listar_emprestimos_usuario(usuario: Usuario, emprestimos: List[Emprestimo]) -> List[Emprestimo]:
    """Retorna todos os empréstimos ativos de um usuário."""
    return [e for e in emprestimos if e.usuario.cpf == usuario.cpf]
