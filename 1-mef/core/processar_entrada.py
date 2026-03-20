def processar_entrada(maquina: dict, entrada: int) -> tuple:
    estado_anterior = maquina["estado_atual"]

    proximo_estado = maquina["TE"][estado_anterior][entrada]

    maquina["estado_atual"] = proximo_estado

    saida = maquina["VS"][proximo_estado]

    return (estado_anterior, entrada, proximo_estado, saida)
