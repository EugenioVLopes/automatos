from exemplos import criar_maquina_1, criar_maquina_2
from display import exibir_maquina, executar_maquina_interativa

def main():
    print("SIMULADOR DE MÁQUINA DE ESTADOS FINITOS (MEF)\n")

    while True:
        print("  1 - Máquina 1")
        print("  2 - Máquina 2")
        print("  0 - Sair")

        opcao = input("\n  Escolha uma opção: ").strip()

        if opcao == "0":
            print("\n  Programa encerrado.")
            break

        elif opcao == "1":
            maq1 = criar_maquina_1()
            exibir_maquina(maq1)
            executar_maquina_interativa(maq1)

        elif opcao == "2":
            maq2 = criar_maquina_2()
            exibir_maquina(maq2)
            executar_maquina_interativa(maq2)

        else:
            print("[ERRO] Opção inválida! Digite 0, 1 ou 2.")


if __name__ == "__main__":
    main()
