emails = ["ana@gmail.com", "", None, "carlos@yahoo.com "]

validos = [email for email in emails if email]

print(validos)

# validos = []

# for email in emails:
#     if email:
#         validos.append(email)

# print(validos)

# crear una lista de numeros al cuadrado

numeros = [1, 2, 3, 4, 5]

cuadrados = [num ** 2 for num in numeros if num % 2 == 0]
print(cuadrados)


# filtrar numeros pares

juego_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = [num for num in juego_numeros if num % 2 == 0]

print(numeros_pares)
