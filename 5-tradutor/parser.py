from __future__ import annotations

from lexer import Token


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.pos = 0
        self.temp_count = 0
        self.code: list[str] = []

    def _novo_temp(self) -> str:
        self.temp_count += 1
        return f"temp{self.temp_count}"

    def _emit(self, dst: str, op: str, a: str, b: str) -> None:
        self.code.append(f"  {dst} = {a} {op} {b}")

    def _token_atual(self) -> Token:
        return self.tokens[self.pos]

    def _consome(self, tipo: str) -> Token:
        token = self._token_atual()
        if token.tipo != tipo:
            raise SyntaxError(
                f"esperado '{tipo}', obtido '{token.tipo}' ('{token.valor}')"
            )
        self.pos += 1
        return token

    # E  → T E'
    def E(self) -> str:
        esquerda = self.T()
        return self._E1(esquerda)

    # E' → + T E' | ε
    def _E1(self, acumulado: str) -> str:
        if self._token_atual().tipo == "MAIS":
            self._consome("MAIS")
            direita = self.T()
            temp = self._novo_temp()
            self._emit(temp, "+", acumulado, direita)
            return self._E1(temp)
        return acumulado

    # T  → F T'
    def T(self) -> str:
        esquerda = self.F()
        return self._T1(esquerda)

    # T' → * F T' | ε
    def _T1(self, acumulado: str) -> str:
        if self._token_atual().tipo == "VEZES":
            self._consome("VEZES")
            direita = self.F()
            temp = self._novo_temp()
            self._emit(temp, "*", acumulado, direita)
            return self._T1(temp)
        return acumulado

    # F → ( E ) | NUM
    def F(self) -> str:
        if self._token_atual().tipo == "ABRE":
            self._consome("ABRE")
            resultado = self.E()
            self._consome("FECHA")
            return resultado
        token = self._consome("NUM")
        temp = self._novo_temp()
        self.code.append(f"  {temp} = {token.valor}")
        return temp

    def parse(self) -> tuple[list[str], str]:
        resultado = self.E()
        self._consome("FIM")
        return self.code, resultado