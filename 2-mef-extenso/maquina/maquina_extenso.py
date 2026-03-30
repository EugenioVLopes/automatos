from core import MaquinaMealy, criar_maquina, processar_entrada

# Vocabulário: índice -> palavra
# 0: ""  (nenhuma palavra / saída vazia)
VOCABULARIO_PORTUGUES = [
    "",  # 0
    "cento",  # 1
    "duzentos",  # 2
    "trezentos",  # 3
    "quatrocentos",  # 4
    "quinhentos",  # 5
    "seiscentos",  # 6
    "setecentos",  # 7
    "oitocentos",  # 8
    "novecentos",  # 9
    "vinte",  # 10
    "trinta",  # 11
    "quarenta",  # 12
    "cinquenta",  # 13
    "sessenta",  # 14
    "setenta",  # 15
    "oitenta",  # 16
    "noventa",  # 17
    "um",  # 18
    "dois",  # 19
    "três",  # 20
    "quatro",  # 21
    "cinco",  # 22
    "seis",  # 23
    "sete",  # 24
    "oito",  # 25
    "nove",  # 26
    "dez",  # 27
    "onze",  # 28
    "doze",  # 29
    "treze",  # 30
    "quatorze",  # 31
    "quinze",  # 32
    "dezesseis",  # 33
    "dezessete",  # 34
    "dezoito",  # 35
    "dezenove",  # 36
]

VOCABULARIO_INGLES_MEF = [
    "",  # 0
    "one hundred",  # 1
    "two hundred",  # 2
    "three hundred",  # 3
    "four hundred",  # 4
    "five hundred",  # 5
    "six hundred",  # 6
    "seven hundred",  # 7
    "eight hundred",  # 8
    "nine hundred",  # 9
    "twenty",  # 10
    "thirty",  # 11
    "forty",  # 12
    "fifty",  # 13
    "sixty",  # 14
    "seventy",  # 15
    "eighty",  # 16
    "ninety",  # 17
    "one",  # 18
    "two",  # 19
    "three",  # 20
    "four",  # 21
    "five",  # 22
    "six",  # 23
    "seven",  # 24
    "eight",  # 25
    "nine",  # 26
    "ten",  # 27
    "eleven",  # 28
    "twelve",  # 29
    "thirteen",  # 30
    "fourteen",  # 31
    "fifteen",  # 32
    "sixteen",  # 33
    "seventeen",  # 34
    "eighteen",  # 35
    "nineteen",  # 36
]


def criar_maquina_extenso() -> MaquinaMealy:
    """
    ni = 9  (entradas: dígitos 0..9)
    no = 36 (saídas: índices 0..36 no VOCABULARIO)
    ns = 4  (estados: s0..s4)

    Layout dos estados (5 estados, contra 41 da versão Moore):
      s0 — estado inicial, espera dígito da centena
      s1 — leu centena, espera dígito da dezena
      s2 — leu dezena normal (t != 1), espera dígito da unidade
      s3 — leu dezena "teen" (t == 1), espera dígito da unidade
      s4 — terminal, leu todos os 3 dígitos
    """
    # Tabela de transição: TE[estado][dígito] -> próximo estado
    TE = [
        # d =  0   1   2   3   4   5   6   7   8   9
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # s0 → sempre vai para s1
        [2, 3, 2, 2, 2, 2, 2, 2, 2, 2],  # s1 → d=1 vai p/ s3 (teen), resto p/ s2
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # s2 → sempre vai para s4
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # s3 → sempre vai para s4
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # s4 → terminal (fica em s4)
    ]

    # A saída depende do estado atual E da entrada (característica de Mealy)
    TS = [
        # d =  0   1   2   3   4   5   6   7   8   9
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],  # s0: centenas (0→"", 1→"cento", ...)
        [0, 0, 10, 11, 12, 13, 14, 15, 16, 17],  # s1: dezenas  (0→"", 1→"" [teen], 2→"vinte", ...)
        [0, 18, 19, 20, 21, 22, 23, 24, 25, 26],  # s2: unidades normais (0→"", 1→"um", ...)
        [27, 28, 29, 30, 31, 32, 33, 34, 35, 36],  # s3: unidades teen (0→"dez", 1→"onze", ...)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # s4: terminal (sem saída)
    ]

    return criar_maquina(ni=9, no=36, ns=4, tabela_transicao=TE, tabela_saida=TS)


def grupo_por_extenso(n: int, maquina: MaquinaMealy) -> list[str]:
    """
    Converte um número de 0 a 999 em lista de palavras usando a MEF.
    Caso especial: 100 → ["cem"].
    """
    if n == 0:
        return []
    if n == 100:
        return ["cem"]

    maquina["estado_atual"] = 0

    centena = n // 100
    dezena = (n % 100) // 10
    unidade = n % 10

    palavras = []
    for digito in (centena, dezena, unidade):
        _, _, _, saida = processar_entrada(maquina, digito)
        if saida != 0:
            palavras.append(VOCABULARIO_PORTUGUES[saida])

    return palavras


def grupo_por_extenso_ingles(n: int, maquina: MaquinaMealy) -> list[str]:
    """Converte um numero de 0 a 999 em lista de palavras em ingles usando a MEF."""
    if n == 0:
        return []

    maquina["estado_atual"] = 0

    centena = n // 100
    dezena = (n % 100) // 10
    unidade = n % 10

    palavras = []
    for digito in (centena, dezena, unidade):
        _, _, _, saida = processar_entrada(maquina, digito)
        if saida != 0:
            palavras.append(VOCABULARIO_INGLES_MEF[saida])

    return palavras


def numero_por_extenso(n: int, maquina: MaquinaMealy) -> str:
    """Converte um inteiro de 0 a 999.999 em sua forma por extenso."""
    if n == 0:
        return "zero"

    milhares = n // 1000
    unidades = n % 1000
    partes = []

    if milhares > 0:
        if milhares == 1:
            partes.append("mil")
        else:
            partes_mil = grupo_por_extenso(milhares, maquina)
            partes.append(" e ".join(partes_mil) + " mil")

    if unidades > 0:
        palavras_unidades = grupo_por_extenso(unidades, maquina)
        partes.append(" e ".join(palavras_unidades))

    # Regra do português: vírgula quando unidades tem centena + algo;
    # "e" quando unidades é só centena exata, dezena ou unidade.
    if len(partes) == 2 and unidades > 100 and unidades % 100 != 0:
        return ", ".join(partes)

    return " e ".join(partes)


def numero_por_extenso_ingles(n: int, maquina: MaquinaMealy) -> str:
    """Converte um inteiro de 0 a 999.999 em sua forma por extenso em ingles."""
    if n == 0:
        return "zero"

    milhares = n // 1000
    unidades = n % 1000
    partes = []

    if milhares > 0:
        if milhares == 1:
            partes.append("one thousand")
        else:
            partes_mil = grupo_por_extenso_ingles(milhares, maquina)
            partes.append(" ".join(partes_mil) + " thousand")

    if unidades > 0:
        palavras_unidades = grupo_por_extenso_ingles(unidades, maquina)
        partes.append(" ".join(palavras_unidades))

    if len(partes) == 2:
        return ", ".join(partes)

    return partes[0]
