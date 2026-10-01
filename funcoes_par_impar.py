def eh_numero_valido(texto):
    """
    Tenta converter texto para número inteiro.
    Retorna True se conseguir, False se der erro (ValueError).
    """
    try:
        int(texto)
        return True
    except ValueError:
        return False


def classificar_parity(numero):
    """
    Recebe um número inteiro e retorna a string 'par' ou 'ímpar'.
    Usa o operador módulo (%) para verificar o resto da divisão por 2.
    """
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"


def main():
    """
    Loop principal do programa.
    Pede entrada ao usuário, valida, classifica e repete até 'sair'.
    """
    print("--- Bem-vindo ao Classificador Par/Ímpar ---")

    while True:
        entrada = input("\nDigite um número (ou 'sair'): ").strip()

        # 1. Verifica comando de saída
        if entrada.lower() == "sair":
            print("Programa encerrado com sucesso. Até logo! 👋")
            break

        # 2. Valida se é um número real usando nossa função auxiliar
        if not eh_numero_valido(entrada):
            print(f"❌ '{entrada}' não é um número válido. Tente novamente.")
            continue  # Volta pro início do loop sem processar mais nada

        # 3. Converte para inteiro seguro
        numero = int(entrada)

        # 4. Usa a função de classificação para obter o resultado
        resultado = classificar_parity(numero)

        # 5. Mostra na tela formatado
        print(f"✅ O número {numero} é {resultado}.")


# Executa o programa apenas quando rodado diretamente
if __name__ == "__main__":
    main()
