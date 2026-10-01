# 1 & 2: Peça dois números ao usuário e guarde cada um numa variável
# int() converte texto digitado em número inteiro (senão vira string!)
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# 3: Some os dois e guarde o resultado numa terceira variável
resultado = num1 + num2

# 4: Mostre na tela uma frase formatada usando f-string (o jeito moderno do Python)
# As chaves {} inserem automaticamente os valores das variáveis ali dentro.
print(f"A soma de {num1} e {num2} é {resultado}")
