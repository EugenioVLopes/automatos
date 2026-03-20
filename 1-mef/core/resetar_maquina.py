def resetar_maquina(maquina: dict) -> None:
    maquina["estado_atual"] = 0
    print("\n  [RESET] Máquina resetada para o estado inicial s0.")
    print(f"  Saída atual: {maquina['VS'][0]}")
