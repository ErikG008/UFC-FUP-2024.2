#programa que verifica paridade#
def par(numero):
    if numero % 2 == 0: 
        print(f"{numero} é par.")
        quadrado = numero ** 2
        print(f"O quadrado de {numero} é {quadrado}, que também é par.")
    else:
        print(f"{numero} é ímpar.")
        quadrado = numero ** 2
        print(f"O quadrado de {numero} é {quadrado}, que não é par.")

numeros = [2, 3, 4, 5, 8, 16, 32, 64, 128, 256, 512]
for numero in numeros:
    par(numero)
