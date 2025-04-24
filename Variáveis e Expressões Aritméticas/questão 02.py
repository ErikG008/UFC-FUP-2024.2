#programa para calcular área e perímetro de um retângulo
a = float(input("digite medida do primeiro lado do retângulo: "))
b = float(input("digite a medida do segundo lado do retângulo: "))

area = a * b
per = 2 * (a + b)

print(f"A área do retângulo é: {area:.2f}")
print(f"O per do retângulo é: {per:.2f}")
