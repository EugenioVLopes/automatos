#!/usr/bin/env python3
"""Simulador interativo de derivação para Gramáticas Livre-do-Contexto (GLC).
"""

import sys

from gramatica import Gramatica
from derivacao import derivacao_interativa, ler_inteiro


def gramatica_0n1n() -> Gramatica:
    """Gramática 1: L(G) = {0^n 1^n : n >= 0}."""
    return Gramatica(
        variaveis={"A", "B"},
        terminais={"0", "1"},
        regras=[
            ("A", "0A1"),
            ("A", "B"),
            ("B", "#"),
        ],
        inicial="A",
    )


def gramatica_palindromos() -> Gramatica:
    """Gramática 2: Palíndromos sobre {a, b}."""
    return Gramatica(
        variaveis={"S"},
        terminais={"a", "b"},
        regras=[
            ("S", "aSa"),
            ("S", "bSb"),
            ("S", "a"),
            ("S", "b"),
            ("S", "#"),
        ],
        inicial="S",
    )


def menu() -> None:
    print("=" * 64)
    print("Simulador de Derivação de GLC")
    print("=" * 64)
    while True:
        print("\nEscolha a gramática:")
        print(" [1] L = {0^n 1^n : n >= 0}")
        print(" [2] Palíndromos sobre {a, b}")
        print(" [0] Sair\n")
        opcao = ler_inteiro("Opção: ", 0, 2)
        if opcao == 0:
            print("Encerrando.")
            return
        try:
            gramatica = gramatica_0n1n() if opcao == 1 else gramatica_palindromos()
        except ValueError as erro:
            print(f"Erro ao construir a gramática: {erro}")
            continue
        derivacao_interativa(gramatica)


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nEncerrado pelo usuário.")
        sys.exit(0)
