num1 = float(input("Escolha um número: "))
op = input("Escolha um operador: ")
num2 = float(input("Escolha outro número: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Opedor inválido")