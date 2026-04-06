from core import MaquinaMealy
from maquina import criar_maquina_extenso, numero_por_extenso, PORTUGUES, INGLES

MENSAGEM_ERRO = (
    "Entrada inválida (só respondo se a entrada for um número entre 0 e 999.999)."
)


def modo_interativo(maquina: MaquinaMealy) -> None:
    print("Digite um número de 0 a 999.999 (ou 'sair' para encerrar).")
    while True:
        entrada = input("\n> ").strip()
        if entrada.lower() in ("sair", "exit", "q"):
            break
        try:
            numero = int(entrada)
            if not (0 <= numero <= 999_999):
                print(MENSAGEM_ERRO)
                continue
            print(f"PT: {numero_por_extenso(numero, maquina, PORTUGUES)}.")
            print(f"EN: {numero_por_extenso(numero, maquina, INGLES)}.")
        except ValueError:
            print(MENSAGEM_ERRO)


def main() -> None:
    maquina = criar_maquina_extenso()
    modo_interativo(maquina)


if __name__ == "__main__":
    main()
