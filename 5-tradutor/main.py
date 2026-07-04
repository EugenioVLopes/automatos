#!/usr/bin/env python3

from lexer import lexar
from parser import Parser


def avaliar(code: list[str], resultado_var: str) -> float:
    env: dict[str, float] = {}
    for linha in code:
        partes = linha.strip().split()
        # formato: "  t1 = 5"  ou  "  t1 = t2 + t3"
        dst = partes[0]
        if len(partes) == 3:
            env[dst] = float(partes[2])
        else:
            a = float(env[partes[2]]) if partes[2] in env else float(partes[2])
            b = float(env[partes[4]]) if partes[4] in env else float(partes[4])
            env[dst] = a + b if partes[3] == "+" else a * b
    return env[resultado_var]


def main() -> None:
    print("Tradutor de Expressões Aritméticas")
    print("Digite uma expressão (ou 'sair' para encerrar)\n")
    while True:
        try:
            entrada = input("expr > ").strip()
        except EOFError:
            print()
            break
        if not entrada:
            continue
        if entrada.lower() in ("sair", "quit", "exit"):
            break
        try:
            tokens = lexar(entrada)
            parser = Parser(tokens)
            code, resultado_var = parser.parse()
            valor = avaliar(code, resultado_var)
            print("\nCódigo 3-endereços:")
            print("\n".join(code))
            print(f"\nResultado: {valor}\n")
        except SyntaxError as e:
            print(f"Erro: {e}\n")


if __name__ == "__main__":
    main()