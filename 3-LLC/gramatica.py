"""Modelo de Gramática Livre-do-Contexto G = <V, Sigma, R, S>.

Convenções:
 * Variáveis (V): uma letra MAIÚSCULA por símbolo (A-Z).
 * Terminais (Sigma): uma letra minúscula (a-z) ou um dígito (0-9).
 * '#' no lado direito de uma regra denota a cadeia vazia (epsilon).
"""

from __future__ import annotations

from typing import List, Set, Tuple

SIMBOLO_VAZIO = "#"  # marcador textual para epsilon nas regras


class Gramatica:
    """Gramática Livre-do-Contexto G = <V, Sigma, R, S>."""

    def __init__(
        self,
        variaveis: Set[str],
        terminais: Set[str],
        regras: List[Tuple[str, str]],
        inicial: str,
    ) -> None:
        # --- validações estruturais --------------------------------------#
        if not variaveis:
            raise ValueError("Conjunto de variáveis não pode ser vazio.")
        if inicial not in variaveis:
            raise ValueError(
                f"Variável inicial '{inicial}' não pertence ao conjunto V."
            )
        if variaveis & terminais:
            raise ValueError(
                "V e Sigma devem ser disjuntos."
                f" Interseção encontrada: {variaveis & terminais}."
            )
        for variavel in variaveis:
            if not (len(variavel) == 1 and variavel.isalpha() and variavel.isupper()):
                raise ValueError(
                    f"Variável inválida: '{variavel}'."
                    " Deve ser uma única letra maiúscula (A-Z)."
                )
        for terminal in terminais:
            if not (len(terminal) == 1 and (terminal.islower() or terminal.isdigit())):
                raise ValueError(
                    f"Terminal inválido: '{terminal}'."
                    " Deve ser uma única letra minúscula (a-z) ou dígito (0-9)."
                )
        for lado_esquerdo, lado_direito in regras:
            if lado_esquerdo not in variaveis:
                raise ValueError(
                    f"Lado esquerdo '{lado_esquerdo}' não pertence ao conjunto V."
                )
            if lado_direito != SIMBOLO_VAZIO:
                for simbolo in lado_direito:
                    if simbolo not in variaveis and simbolo not in terminais:
                        raise ValueError(
                            f"Símbolo '{simbolo}' em"
                            f" '{lado_esquerdo} -> {lado_direito}'"
                            " não pertence a V ∪ Sigma."
                        )

        self.variaveis: Set[str] = set(variaveis)
        self.terminais: Set[str] = set(terminais)
        self.regras: List[Tuple[str, str]] = list(regras)
        self.inicial: str = inicial

    def descricao(self) -> str:
        """Representação textual da gramática."""
        linhas = [
            f" V     = {{{', '.join(sorted(self.variaveis))}}}",
            f" Sigma = {{{', '.join(sorted(self.terminais))}}}",
            f" S     = {self.inicial}",
            " R:",
        ]
        for indice, (lado_esquerdo, lado_direito) in enumerate(self.regras, start=1):
            lado_direito_exibicao = (
                "ε" if lado_direito == SIMBOLO_VAZIO else lado_direito
            )
            linhas.append(f" ({indice}) {lado_esquerdo} -> {lado_direito_exibicao}")
        return "\n".join(linhas)
