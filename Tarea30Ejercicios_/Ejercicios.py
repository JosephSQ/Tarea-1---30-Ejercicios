#Joseph Quevedo



    # Ejercicio 1
print("Holaaaaaaaaaaaaa, ya se imprimir frases")

    # Ejercicio 2
print(273)

# Ejercicio 3
print(5.3)

# Ejercicio 4
print(1234 + 532)

# Ejercicio 5
print(1234 - 532)

# Ejercicio 6
print(1234 * 532)

# Ejercicio 7
print(1234 / 532)

# Ejercicio 8
for i in range(1, 4):
    print(i)

# Ejercicio 9
for i in range(1, 10):
    print(i)

# Ejercicio 10
for i in range(1, 10001):
    print(i)

# Ejercicio 11
for i in range(5, 11):
    print(i)

# Ejercicio 12
for i in range(5, 16):
    print(i)

# Ejercicio 13
for i in range(5, 15001):
    print(i)

# Ejercicio 14
h = "hola"
for _ in range(200):
    print(h)

# Ejercicio 15
for i in range(1, 31):
    print(i * i)

# Ejercicio 16
r = 1
for i in range(1, 21):
    r *= i
print(r)

# Ejercicio 17
print(sum(i * i for i in range(1, 101)))

# Ejercicio 18
n = int(input("Número: "))
print(sum(range(n + 1, n + 101)))

# Ejercicio 19
euros = float(input("Euros: "))
tasa = float(input("Tasa de cambio: "))
print(euros * tasa)

# Ejercicio 20
alto = float(input("Altura: "))
ancho = float(input("Anchura: "))
print(alto * ancho)

# Ejercicio 21
a = int(input("Número 1: "))
b = int(input("Número 2: "))
print("Mayor:", max(a, b), "Menor:", min(a, b))

# Ejercicio 22
n = int(input("Hasta qué número (impares): "))
for i in range(1, n, 2):
    print(i)

# Ejercicio 23
a = int(input("Número A: "))
b = int(input("Número B: "))
while b:
    a, b = b, a % b
print("GCD:", a)

# Ejercicio 24
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = b * b - 4 * a * c
if d < 0:
    print("Sin solución")
elif d == 0:
    print("Raíz:", -b / (2 * a))
else:
    r1 = (-b + d ** 0.5) / (2 * a)
    r2 = (-b - d ** 0.5) / (2 * a)
    print("Raíces:", r1, r2)

# Ejercicio 25
def fact(n):
    return 1 if n == 0 else n * fact(n - 1)

def ack(x, y):
    if x == 0:
        return y + 1
    if y == 0:
        return ack(x - 1, 1)
    return ack(x - 1, ack(x, y - 1))

print("Factorial(5):", fact(5))
print("Ackermann(2,2):", ack(2, 2))

# Ejercicio 26
a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))
print("Mayor:", max(a, b, c), "Menor:", min(a, b, c))

# Ejercicio 27
while True:
    f = float(input("Fahrenheit: "))
    if f == 999:
        break
    print("Celsius:", (f - 32) * 5 / 9)

# Ejercicio 28
for i in range(3):
    if i == 0:
        print("Cero")
    elif i == 1:
        print("Uno")
    elif i == 2:
        print("Dos")

# Ejercicio 29
try:
    while True:
        input()
except EOFError:
    print("Fin de archivo detectado")

# Ejercicio 30
for i in range(2, 100):
    primo = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i)
