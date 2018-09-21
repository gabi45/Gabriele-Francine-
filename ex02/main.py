import math

a=int(input("informe valor de a: "))
b= int (input("informe valor de b: "))
c= int(input("informe o valor de C:"))

delta = b * b - 4 * a * c

print("Delta: ", delta )

if delta>=0:
    x1= (-b + math.sqrt(delta)) / (2 * a)
    x2= (-b - math.sqrt(delta))/ (2 * a)
    print("raiz ex01: ", x1)
    print("raiz x2: ", x2)
else:
    print("Nao existem raizes reais")

