def exibir_maquina(maquina: dict) -> None:
    ni = maquina["ni"]
    ns = maquina["ns"]
    TE = maquina["TE"]
    VS = maquina["VS"]

    print(f"\n  Conjunto de entradas  I = {{0, ..., {ni}}}")
    print(f"  Conjunto de saídas    O = {{0, ..., {maquina['no']}}}")
    print(f"  Conjunto de estados   S = {{s0, ..., s{ns}}}")
    print(f"  Estado inicial        : s0")
    print(f"\n  Tabela de Transição TE[{ns + 1}][{ni + 1}]:")
    print("  " + "-" * (16 + 10 * (ni + 1)))

    cabecalho = "  Estado\\Entrada |"
    for i in range(ni + 1):
        cabecalho += f"    {i}    "
    print(cabecalho)
    print("  " + "-" * (16 + 10 * (ni + 1)))

    for s in range(ns + 1):
        linha = f"       s{s}        |"
        for i in range(ni + 1):
            linha += f"   s{TE[s][i]}    "
        print(linha)

    print("  " + "-" * (16 + 10 * (ni + 1)))

    print(f"\n  Vetor de Saída VS[{ns + 1}]:")
    for s in range(ns + 1):
        print(f"    VS[s{s}] = {VS[s]}  (estado s{s} produz saída {VS[s]})")

    print("=" * 60)
