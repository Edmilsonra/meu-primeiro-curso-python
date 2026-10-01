# 1. Peça um número ao usuário e converta para inteiro
numero = int(input("Digite um número: "))

# 2. Verifique se é par usando o operador módulo (%)
# % retorna o RESTO da divisão. Se dividir por 2 e der resto 0 → é PAR.
if numero % 2 == 0:
    print(f"{numero} é um número PAR.")
else:
    # Se não for par (resto ≠ 0), então é ÍMPAR.
    print(f"{numero} é um número ÍMPAR.")
