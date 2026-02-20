num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == "+":
    print(f"Resultado: {num1 + num2}")
elif operacao == "-":
    print(f"Resultado: {num1 - num2}")
elif operacao == "*":
    print(f"Resultado: {num1 * num2}")
elif operacao == "/":
    print(f"Resultado: {num1 / num2}" if num2 != 0 else "Erro: Divisão por zero")
else:
    print("Operação inválida!")