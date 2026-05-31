"""Motor de derivação passo a passo para Gramáticas Livre-do-Contexto."""

from __future__ import annotations

from typing import List, Tuple

from gramatica import SIMBOLO_VAZIO, Gramatica


def regras_habilitadas(
    gramatica: Gramatica, cadeia: str
) -> List[Tuple[int, int, str, str]]:
    """Lista todas as instâncias (regra, posição) aplicáveis à cadeia atual.

    Retorna uma lista de tuplas (id_regra, posicao, lado_esquerdo,
    lado_direito), onde id_regra é o índice 1-based da regra em
    gramatica.regras. posicao é o índice da ocorrência da variável
    (lado_esquerdo) na cadeia. Esta enumeração permite ao usuário
    escolher não apenas qual regra aplicar, mas também qual ocorrência
    de uma variável (caso ela apareça mais de uma vez).
    """
    habilitadas: List[Tuple[int, int, str, str]] = []
    for id_regra, (lado_esquerdo, lado_direito) in enumerate(gramatica.regras, start=1):
        for posicao, simbolo in enumerate(cadeia):
            if simbolo == lado_esquerdo:
                habilitadas.append((id_regra, posicao, lado_esquerdo, lado_direito))
    return habilitadas


def aplicar_regra(
    cadeia: str, posicao: int, lado_esquerdo: str, lado_direito: str
) -> str:
    """Aplica a substituição lado_esquerdo -> lado_direito na posição dada."""
    substituto = "" if lado_direito == SIMBOLO_VAZIO else lado_direito
    return cadeia[:posicao] + substituto + cadeia[posicao + len(lado_esquerdo) :]


def formatar_cadeia(cadeia: str) -> str:
    """Exibe ε quando a cadeia é vazia, caso contrário a própria cadeia."""
    return cadeia if cadeia else "ε"


def derivacao_interativa(gramatica: Gramatica) -> None:
    """Executa a derivação passo a passo com o usuário."""
    print("\n" + "=" * 64)
    print("Gramática carregada:")
    print(gramatica.descricao())
    print("=" * 64)

    cadeia: str = gramatica.inicial
    passo: int = 0
    historico: List[str] = [cadeia]

    print(f"\nEstado inicial: {formatar_cadeia(cadeia)}")

    while True:
        habilitadas = regras_habilitadas(gramatica, cadeia)

        # --- critério de parada: nenhuma regra habilitada ---------------#
        if not habilitadas:
            print("\nNão há mais regras habilitadas – derivação encerrada.")
            print(f"Cadeia final: {formatar_cadeia(cadeia)}")
            print(f"Passos totais: {passo}")
            print("Trajetória: " + " => ".join(formatar_cadeia(c) for c in historico))
            return

        # --- exibe as regras habilitadas e solicita escolha -------------#
        print(f"\n----- Passo {passo + 1} -----")
        print(f"Cadeia atual: {formatar_cadeia(cadeia)}")
        print("Opções de aplicação:")
        for opcao, (id_regra, posicao, lado_esquerdo, lado_direito) in enumerate(
            habilitadas, start=1
        ):
            lado_direito_exibicao = (
                "ε" if lado_direito == SIMBOLO_VAZIO else lado_direito
            )
            print(
                f" [{opcao:2d}] regra ({id_regra}):"
                f" {lado_esquerdo} -> {lado_direito_exibicao}"
                f" (aplicada na posição {posicao})"
            )
        print("  [0] encerrar derivação")

        escolha = ler_inteiro("Escolha uma opção: ", 0, len(habilitadas))
        if escolha == 0:
            print(f"\nDerivação interrompida. Cadeia atual: {formatar_cadeia(cadeia)}")
            print("Trajetória: " + " => ".join(formatar_cadeia(c) for c in historico))
            return

        # --- aplica a regra escolhida ----------------------------------#
        id_regra, posicao, lado_esquerdo, lado_direito = habilitadas[escolha - 1]
        nova_cadeia = aplicar_regra(cadeia, posicao, lado_esquerdo, lado_direito)
        lado_direito_exibicao = "ε" if lado_direito == SIMBOLO_VAZIO else lado_direito
        print(
            f"\n{formatar_cadeia(cadeia)} =>"
            f" {formatar_cadeia(nova_cadeia)}"
            f" [regra ({id_regra}):"
            f" {lado_esquerdo} -> {lado_direito_exibicao},"
            f" posição {posicao}]"
        )
        cadeia = nova_cadeia
        historico.append(cadeia)
        passo += 1


def ler_inteiro(mensagem: str, minimo: int, maximo: int) -> int:
    """Lê um inteiro do teclado dentro do intervalo [minimo, maximo]."""
    while True:
        try:
            valor = int(input(mensagem).strip())
        except (ValueError, EOFError):
            print(" Entrada inválida – informe um número inteiro.")
            continue
        if valor < minimo or valor > maximo:
            print(f" Valor fora do intervalo permitido [{minimo}, {maximo}].")
            continue
        return valor
