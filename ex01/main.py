import math

x1= int(input("coordenada ex01 de P1: "))
y1= int(input("coordenada ex02 de P1: "))
x2= int(input("coordenada x2 de P2: "))
y2= int(input("coordenada y2 de P2 "))

d = math.sqrt( (x1-x2)**2 + (y1-y2)**2)

print("distancia entre P1 e P2 e: ", d)
