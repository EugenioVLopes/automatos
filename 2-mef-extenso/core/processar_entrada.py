from .tipos import MaquinaMealy


def processar_entrada(maquina: MaquinaMealy, entrada: int) -> tuple[int, int, int, int]:
    estado_anterior = maquina["estado_atual"]

    proximo_estado = maquina["TE"][estado_anterior][entrada]

    # Mealy: saída depende do estado atual E da entrada
    saida = maquina["TS"][estado_anterior][entrada]

    maquina["estado_atual"] = proximo_estado

    return (estado_anterior, entrada, proximo_estado, saida)
