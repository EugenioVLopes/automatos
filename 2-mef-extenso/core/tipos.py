from typing import TypeAlias, TypedDict

TabelaInteiros: TypeAlias = list[list[int]]


class MaquinaMealy(TypedDict):
    ni: int
    no: int
    ns: int
    TE: TabelaInteiros
    TS: TabelaInteiros
    estado_atual: int
