from core import criar_maquina


def criar_maquina_1():
    ni = 1  # Entradas: {0, 1}
    no = 1  # Saídas: {0, 1}
    ns = 2  # Estados: {s0, s1, s2}

    TE = [
        [0, 1],  # s0: 0 → s0, 1 → s1
        [2, 1],  # s1: 0 → s2, 1 → s1
        [2, 0],  # s2: 0 → s2, 1 → s0
    ]

    VS = [0, 1, 1]  # s0 → 0, s1 → 1, s2 → 1

    return criar_maquina(ni, no, ns, TE, VS)
