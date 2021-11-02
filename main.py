print(f"------------ Calculadora Python ---------------")

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print(f"Digite qual operação deseja fazer!")
print(f"1 - Somar")
print(f"2 - Subtrair")
print(f"3 - Multiplicar")
print(f"4 - Dividir")
operador = int(input(f"Digite ( 1 / 2 / 3 / 4 ): "))

if operador < 1 or operador > 4:
    print("opção inválida!")
else:
    x = int(input(f"Digite o primeiro número: "))
    y = int(input(f"Digite o segundo número: "))
    if operador == 1:
        print(x, "+", y, "=", soma(x,y))
    elif operador == 2:
        print(x, "-", y, "=", sub(x,y))
    elif operador == 3:
        print(x, "*", y, "=", mul(x,y))
    elif operador == 4:
        print(x, "/", y, "=", div(x,y))
