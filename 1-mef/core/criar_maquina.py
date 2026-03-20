def criar_maquina(ni: int, no: int, ns: int, tabela_transicao: list[list[int]], vetor_saida: list[int]) -> dict:
    if ni < 0 or no < 0 or ns < 0:
        raise ValueError("ni, no e ns devem ser inteiros positivos (>= 0).")

    if len(tabela_transicao) != ns + 1:
        raise ValueError(
            f"Tabela de transição deve ter {ns + 1} linhas (uma por estado), "
            f"mas tem {len(tabela_transicao)}."
        )

    for idx, linha in enumerate(tabela_transicao):
        if len(linha) != ni + 1:
            raise ValueError(
                f"Linha {idx} da tabela de transição deve ter {ni + 1} colunas, "
                f"mas tem {len(linha)}."
            )

    if len(vetor_saida) != ns + 1:
        raise ValueError(
            f"Vetor de saída deve ter {ns + 1} elementos, "
            f"mas tem {len(vetor_saida)}."
        )

    for s in range(ns + 1):
        for i in range(ni + 1):
            prox = tabela_transicao[s][i]
            if prox < 0 or prox > ns:
                raise ValueError(
                    f"Transição inválida: TE[{s}][{i}] = {prox}, "
                    f"mas o estado deve estar entre 0 e {ns}."
                )

    for s in range(ns + 1):
        if vetor_saida[s] < 0 or vetor_saida[s] > no:
            raise ValueError(
                f"Saída inválida: VS[{s}] = {vetor_saida[s]}, "
                f"mas a saída deve estar entre 0 e {no}."
            )

    maquina = {
        "ni": ni,
        "no": no,
        "ns": ns,
        "TE": tabela_transicao,
        "VS": vetor_saida,
        "estado_atual": 0,
    }

    return maquina
