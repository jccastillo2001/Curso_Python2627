nombres = ["ana", "jose", "pedro", "maria", "jorge", "javier"]

print(nombres[1:6])
print(nombres[0:6:2])
print(nombres[::2])
print(nombres[::-1])
print(nombres[:6])


emails = ["ana@gmail.com", "carlos@yahoo.com", "pedro@gmail.com"]

email_validos = [email[:email.index("@")] for email in emails]

print(email_validos)
