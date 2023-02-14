nomecompleto = input('Digite seu nome: ')

print("Seu nome com todas a letras maiúscula fica: ", nomecompleto.upper())
print("Seu nome com todas a letras minúsculas fica: ", nomecompleto.lower())
print("Total de letras em seu nome sem contar os espaços: ", len(nomecompleto.strip()))
dividido = nomecompleto.split()
print("Total de letras no primeiro nome: ", len(dividido[0].strip()))
