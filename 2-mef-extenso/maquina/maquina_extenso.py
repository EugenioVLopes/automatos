from dataclasses import dataclass

from core import MaquinaMealy, criar_maquina, processar_entrada


# ---------------------------------------------------------------------------
# Configuração de idioma
# ---------------------------------------------------------------------------

@dataclass
class Idioma:
    vocabulario: list[str]
    mil_singular: str       # palavra para 1.000 exatos
    sufixo_mil: str         # sufixo para N * 1.000 (N > 1)
    separador_grupo: str    # une partes dentro do grupo de 3 dígitos
    separador_milhar: str   # une grupo dos milhares com o restante
    cem: str | None         # forma especial para 100 exato (None = sem caso especial)


PORTUGUES = Idioma(
    vocabulario=[
        "",           # 0  — saída vazia
        "cento",      # 1
        "duzentos",   # 2
        "trezentos",  # 3
        "quatrocentos",  # 4
        "quinhentos",    # 5
        "seiscentos",    # 6
        "setecentos",    # 7
        "oitocentos",    # 8
        "novecentos",    # 9
        "vinte",      # 10
        "trinta",     # 11
        "quarenta",   # 12
        "cinquenta",  # 13
        "sessenta",   # 14
        "setenta",    # 15
        "oitenta",    # 16
        "noventa",    # 17
        "um",         # 18
        "dois",       # 19
        "três",       # 20
        "quatro",     # 21
        "cinco",      # 22
        "seis",       # 23
        "sete",       # 24
        "oito",       # 25
        "nove",       # 26
        "dez",        # 27
        "onze",       # 28
        "doze",       # 29
        "treze",      # 30
        "quatorze",   # 31
        "quinze",     # 32
        "dezesseis",  # 33
        "dezessete",  # 34
        "dezoito",    # 35
        "dezenove",   # 36
    ],
    mil_singular="mil",
    sufixo_mil=" mil",
    separador_grupo=" e ",
    separador_milhar=" e ",
    cem="cem",
)

INGLES = Idioma(
    vocabulario=[
        "",             # 0
        "one hundred",  # 1
        "two hundred",  # 2
        "three hundred",   # 3
        "four hundred",    # 4
        "five hundred",    # 5
        "six hundred",     # 6
        "seven hundred",   # 7
        "eight hundred",   # 8
        "nine hundred",    # 9
        "twenty",   # 10
        "thirty",   # 11
        "forty",    # 12
        "fifty",    # 13
        "sixty",    # 14
        "seventy",  # 15
        "eighty",   # 16
        "ninety",   # 17
        "one",      # 18
        "two",      # 19
        "three",    # 20
        "four",     # 21
        "five",     # 22
        "six",      # 23
        "seven",    # 24
        "eight",    # 25
        "nine",     # 26
        "ten",      # 27
        "eleven",   # 28
        "twelve",   # 29
        "thirteen", # 30
        "fourteen", # 31
        "fifteen",  # 32
        "sixteen",  # 33
        "seventeen",# 34
        "eighteen", # 35
        "nineteen", # 36
    ],
    mil_singular="one thousand",
    sufixo_mil=" thousand",
    separador_grupo=" ",
    separador_milhar=", ",
    cem=None,
)


# ---------------------------------------------------------------------------
# Criação da MEF (única, compartilhada entre idiomas)
# ---------------------------------------------------------------------------

def criar_maquina_extenso() -> MaquinaMealy:
    """
    Cria a MEF de Mealy para converter grupos de 3 dígitos.

    Estados (5 no total, contra 41 da versão Moore):
      s0 — inicial, espera dígito da centena
      s1 — leu centena, espera dígito da dezena
      s2 — leu dezena normal (t != 1), espera dígito da unidade
      s3 — leu dezena "teen" (t == 1), espera dígito da unidade
      s4 — terminal

    Entradas: dígitos 0–9  (ni = 9)
    Saídas:   índices 0–36 no vocabulário  (no = 36)
    """
    TE = [
        # d =  0   1   2   3   4   5   6   7   8   9
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # s0 → s1
        [2, 3, 2, 2, 2, 2, 2, 2, 2, 2],  # s1 → d=1: s3 (teen), resto: s2
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # s2 → s4
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # s3 → s4
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # s4 → s4 (terminal)
    ]

    TS = [
        # d =  0   1   2   3   4   5   6   7   8   9
        [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],  # s0: centenas
        [ 0,  0, 10, 11, 12, 13, 14, 15, 16, 17],  # s1: dezenas (1→"" pois é teen)
        [ 0, 18, 19, 20, 21, 22, 23, 24, 25, 26],  # s2: unidades normais
        [27, 28, 29, 30, 31, 32, 33, 34, 35, 36],  # s3: dezenas teen (10–19)
        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # s4: terminal
    ]

    return criar_maquina(ni=9, no=36, ns=4, tabela_transicao=TE, tabela_saida=TS)


# ---------------------------------------------------------------------------
# Conversão de grupos de 3 dígitos
# ---------------------------------------------------------------------------

def grupo_por_extenso(n: int, maquina: MaquinaMealy, idioma: Idioma) -> list[str]:
    """Converte um número de 0 a 999 em lista de palavras usando a MEF."""
    if n == 0:
        return []
    if idioma.cem is not None and n == 100:
        return [idioma.cem]

    maquina["estado_atual"] = 0
    centena = n // 100
    dezena = (n % 100) // 10
    unidade = n % 10

    palavras = []
    for digito in (centena, dezena, unidade):
        _, _, _, saida = processar_entrada(maquina, digito)
        if saida != 0:
            palavras.append(idioma.vocabulario[saida])

    return palavras


# ---------------------------------------------------------------------------
# Conversão de 0 a 999.999
# ---------------------------------------------------------------------------

def numero_por_extenso(n: int, maquina: MaquinaMealy, idioma: Idioma) -> str:
    """Converte um inteiro de 0 a 999.999 em sua forma por extenso."""
    if n == 0:
        return "zero"

    milhares = n // 1000
    unidades = n % 1000
    partes = []

    if milhares > 0:
        if milhares == 1:
            partes.append(idioma.mil_singular)
        else:
            partes_mil = grupo_por_extenso(milhares, maquina, idioma)
            partes.append(idioma.separador_grupo.join(partes_mil) + idioma.sufixo_mil)

    if unidades > 0:
        palavras_unidades = grupo_por_extenso(unidades, maquina, idioma)
        partes.append(idioma.separador_grupo.join(palavras_unidades))

    # Português: vírgula quando há centena + algo além da centena
    if idioma is PORTUGUES and len(partes) == 2 and unidades > 100 and unidades % 100 != 0:
        return ", ".join(partes)

    return idioma.separador_milhar.join(partes)
