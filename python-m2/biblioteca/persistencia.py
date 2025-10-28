
import json
from pathlib import Path
from typing import List


# BLOCO 1 — CONFIGURAÇÃO DE CAMINHOS
BASE = Path(__file__).parent
DADOS_DIR = BASE / "dados"
DADOS_DIR.mkdir(exist_ok=True)

# BLOCO 2 — FUNÇÕES GENÉRICAS DE JSON
def salvar_json(objetos: List[dict], caminho: Path) -> None:
    """Salva uma lista de dicionários em JSON, com indentação legível."""
    with caminho.open("w", encoding="utf-8") as f:
        json.dump(objetos, f, ensure_ascii=False, indent=2)


def carregar_json(caminho: Path) -> List[dict]:
    """Carrega lista de dicionários de um arquivo JSON. Retorna lista vazia se não existir."""
    if not caminho.exists():
        return []
    with caminho.open("r", encoding="utf-8") as f:
        return json.load(f)

# BLOCO 3 — LIVROS
def salvar_acervo(acervo: List, nome_arquivo: str = "dados/livros.json") -> None:
    """Salva o acervo (lista de livros) no JSON."""
    from livros import Livro
    path = BASE / nome_arquivo
    salvar_json([{
        "titulo": l.titulo,
        "autor": l.autor,
        "ano": l.ano,
        "exemplares": l.exemplares
    } for l in acervo], path)

def carregar_acervo(nome_arquivo: str = "dados/livros.json") -> List:
    """Carrega os livros e retorna uma lista de objetos Livro."""
    from livros import Livro
    path = BASE / nome_arquivo
    dados = carregar_json(path)
    return [Livro(d["titulo"], d["autor"], int(d["ano"]), int(d["exemplares"])) for d in dados]

# BLOCO 4 — USUÁRIOS
def salvar_usuarios(usuarios: List, nome_arquivo: str = "dados/usuarios.json") -> None:
    """Salva os usuários no JSON."""
    from usuarios import Usuario
    path = BASE / nome_arquivo
    salvar_json([{"nome": u.nome, "cpf": u.cpf} for u in usuarios], path)

def carregar_usuarios(nome_arquivo: str = "dados/usuarios.json") -> List:
    """Carrega os usuários e retorna uma lista de objetos Usuario."""
    from usuarios import Usuario
    path = BASE / nome_arquivo
    dados = carregar_json(path)
    return [Usuario(d["nome"], d["cpf"]) for d in dados]

# BLOCO 5 — EMPRÉSTIMOS (AGORA COMPATÍVEL COM OBJETOS)
def salvar_emprestimos(emprestimos: List, nome_arquivo: str = "dados/emprestimos.json") -> None:
    """Salva os empréstimos, gravando apenas o CPF do usuário e o título do livro."""
    from emprestimos import Emprestimo
    path = BASE / nome_arquivo
    salvar_json([{
        "usuario_cpf": e.usuario.cpf,
        "livro_titulo": e.livro.titulo
    } for e in emprestimos], path)


def carregar_emprestimos(usuarios: List, livros: List, nome_arquivo: str = "dados/emprestimos.json") -> List:
    from emprestimos import Emprestimo
    path = BASE / nome_arquivo
    dados = carregar_json(path)
    emprestimos = []
    for d in dados:
        try:
            emp = Emprestimo.from_dict(d, usuarios, livros)
            emprestimos.append(emp)
        except ValueError:
            print(f"Aviso: empréstimo ignorado (usuário ou livro inexistente) → {d}")
    return emprestimos

# BLOCO 6 — SALVAR E CARREGAR TUDO
def salvar_tudo(acervo, usuarios, emprestimos):
    """Salva todos os dados do sistema de uma vez."""
    salvar_acervo(acervo)
    salvar_usuarios(usuarios)
    salvar_emprestimos(emprestimos)

def carregar_tudo():
    usuarios = carregar_usuarios()
    acervo = carregar_acervo()
    emprestimos = carregar_emprestimos(usuarios, acervo)
    return acervo, usuarios, emprestimos
