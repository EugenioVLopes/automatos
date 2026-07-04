from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class Token:
    tipo: str
    valor: str


TOKEN_SPEC = [
    ("NUM", r"\d+(\.\d+)?"),
    ("MAIS", r"\+"),
    ("VEZES", r"\*"),
    ("ABRE", r"\("),
    ("FECHA", r"\)"),
    ("ESPACO", r"\s+"),
]

RE_TOKEN = re.compile("|".join(f"(?P<{t}>{p})" for t, p in TOKEN_SPEC))


def lexar(entrada: str) -> list[Token]:
    tokens: list[Token] = []
    pos = 0
    while pos < len(entrada):
        m = RE_TOKEN.match(entrada, pos)
        if not m:
            raise SyntaxError(f"caractere inesperado: '{entrada[pos]}' na posição {pos}")
        tipo = m.lastgroup
        if tipo != "ESPACO":
            tokens.append(Token(tipo=tipo, valor=m.group()))
        pos = m.end()
    tokens.append(Token(tipo="FIM", valor=""))
    return tokens
