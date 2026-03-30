from .tipos import MaquinaMealy


def resetar_maquina(maquina: MaquinaMealy) -> None:
    maquina["estado_atual"] = 0
    print("\n  [RESET] Máquina resetada para o estado inicial s0.")
