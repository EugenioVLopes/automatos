from core import processar_entrada, resetar_maquina


def executar_maquina_interativa(maquina: dict) -> None:
    ni = maquina["ni"]

    print(f"\n  Entradas válidas: inteiros de 0 a {ni}")
    print("  Digite 'r' para resetar a máquina (voltar ao estado s0)")
    print("  Digite 'q' para encerrar a execução desta máquina")

    ciclo = 0

    print(f"\n  --- Estado Inicial ---")
    print(f"  Estado: s{maquina['estado_atual']}  |  Saída: {maquina['VS'][maquina['estado_atual']]}")
    print()

    while True:
        entrada_str = input(f"  [Ciclo t{ciclo}] Digite a entrada: ").strip()
        if entrada_str.lower() == 'q':
            print("\n  Execução encerrada pelo usuário.")
            break

        if entrada_str.lower() == 'r':
            resetar_maquina(maquina)
            continue

        try:
            entrada = int(entrada_str)
        except ValueError:
            print(f"  [ERRO] Entrada inválida: '{entrada_str}'")
            print(f"         A máquina só aceita valores de 0 a {ni} ou 'r' para reset.")
            continue

        if entrada < 0 or entrada > ni:
            print(f"  [ERRO] Entrada {entrada} fora do intervalo!")
            print(f"         A entrada deve ser um valor entre 0 e {ni}.")
            continue

        estado_ant, ent, prox_estado, saida = processar_entrada(maquina, entrada)
        print(f"    Entrada:  {ent}")
        print(f"    Estado:   s{estado_ant} → s{prox_estado}")
        print(f"    Saída:    {saida}")

        ciclo += 1
