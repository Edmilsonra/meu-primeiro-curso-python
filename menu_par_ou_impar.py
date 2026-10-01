def eh_numero_valido(texto):
    try:
        int(texto)
        return True
    except ValueError:
        return False


def classificar_parity(numero):
    if numero % 2 == 0:
        return "par"
    return "ímpar"


while True:
    entrada = input("Digite um número (ou 'sair'): ")

    if entrada.lower() == "sair":
        print("Programa encerrado.")
        break

    if not eh_numero_valido(entrada):
        print(f"'{entrada}' não é um número válido. Digite apenas dígitos ou 'sair'.")
        continue

    numero = int(entrada)
    print(f"{numero} é {classificar_parity(numero)}")
