from .tipos import MaquinaMealy, TabelaInteiros


def criar_maquina(
    ni: int,
    no: int,
    ns: int,
    tabela_transicao: TabelaInteiros,
    tabela_saida: TabelaInteiros,
) -> MaquinaMealy:
    """
    Cria uma Máquina de Mealy.

    Parâmetros:
        ni: maior índice de entrada (entradas vão de 0 a ni)
        no: maior índice de saída (saídas vão de 0 a no)
        ns: maior índice de estado (estados vão de 0 a ns)
        tabela_transicao: TE[estado][entrada] → próximo estado
        tabela_saida: TS[estado][entrada] → saída (Mealy: depende do estado E da entrada)
    """
    if ni < 0 or no < 0 or ns < 0:
        raise ValueError("ni, no e ns devem ser inteiros positivos (>= 0).")

    if len(tabela_transicao) != ns + 1:
        raise ValueError(
            f"Tabela de transição deve ter {ns + 1} linhas (uma por estado), "
            f"mas tem {len(tabela_transicao)}."
        )

    if len(tabela_saida) != ns + 1:
        raise ValueError(
            f"Tabela de saída deve ter {ns + 1} linhas (uma por estado), "
            f"mas tem {len(tabela_saida)}."
        )

    for idx in range(ns + 1):
        if len(tabela_transicao[idx]) != ni + 1:
            raise ValueError(
                f"Linha {idx} da tabela de transição deve ter {ni + 1} colunas, "
                f"mas tem {len(tabela_transicao[idx])}."
            )
        if len(tabela_saida[idx]) != ni + 1:
            raise ValueError(
                f"Linha {idx} da tabela de saída deve ter {ni + 1} colunas, "
                f"mas tem {len(tabela_saida[idx])}."
            )

    for s in range(ns + 1):
        for i in range(ni + 1):
            prox = tabela_transicao[s][i]
            if prox < 0 or prox > ns:
                raise ValueError(
                    f"Transição inválida: TE[{s}][{i}] = {prox}, "
                    f"mas o estado deve estar entre 0 e {ns}."
                )
            saida = tabela_saida[s][i]
            if saida < 0 or saida > no:
                raise ValueError(
                    f"Saída inválida: TS[{s}][{i}] = {saida}, "
                    f"mas a saída deve estar entre 0 e {no}."
                )

    maquina: MaquinaMealy = {
        "ni": ni,
        "no": no,
        "ns": ns,
        "TE": tabela_transicao,
        "TS": tabela_saida,
        "estado_atual": 0,
    }

    return maquina
