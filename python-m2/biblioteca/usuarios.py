from typing import Dict, List


class Usuario:
    """Representa um usuário da biblioteca."""

    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    def to_dict(self) -> Dict:
        """Converte o usuário para dicionário (para salvar em arquivo)."""
        return {"nome": self.nome, "cpf": self.cpf}

    @staticmethod
    def from_dict(d: Dict) -> 'Usuario':
        """Cria um usuário a partir de um dicionário."""
        return Usuario(d["nome"], d["cpf"])


def cadastrar_usuario(lista_usuarios: List[Usuario], nome: str, cpf: str) -> Usuario:
    """Cadastra um novo usuário, evitando duplicatas de CPF."""
    for u in lista_usuarios:
        if u.cpf == cpf:
            raise ValueError("Já existe um usuário com este CPF.")
    novo = Usuario(nome, cpf)
    lista_usuarios.append(novo)
    return novo


def buscar_usuario_por_cpf(lista_usuarios: List[Usuario], cpf: str) -> Usuario | None:
    """Retorna um usuário com o CPF informado, ou None se não existir."""
    for u in lista_usuarios:
        if u.cpf == cpf:
            return u
    return None
