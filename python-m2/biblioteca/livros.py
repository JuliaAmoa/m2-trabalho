from typing import Dict, List, Optional

class Livro:
    def __init__(self, titulo: str, autor: str, ano: int, exemplares: int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.exemplares = exemplares

def to_dict(self) -> Dict:
    return {
    "titulo": self.titulo,
    "autor": self.autor,
    "ano": self.ano,
    "exemplares": self.exemplares,
    }
@staticmethod
def from_dict(d: Dict) -> 'Livro':
    return Livro(d["titulo"], d["autor"], int(d["ano"]), int(d["exemplares"]))

def cadastrar_livro(acervo: List[Livro], titulo: str, autor: str, ano: int, exemplares: int) -> Livro:

    for livro in acervo:
        if livro.titulo.lower() == titulo.lower() and livro.autor.lower() == autor.lower():
            livro.exemplares += exemplares
    return livro
    novo = Livro(titulo, autor, ano, exemplares)
    acervo.append(novo)
    return novo

def buscar_por_titulo(acervo: List[Livro], termo: str) -> List[Livro]:

    termo = termo.lower()
    return [l for l in acervo if termo in l.titulo.lower()]

def buscar_por_autor(acervo: List[Livro], autor: str) -> List[Livro]:
    autor = autor.lower()
    return [l for l in acervo if autor in l.autor.lower()]