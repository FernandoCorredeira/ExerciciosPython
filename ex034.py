cidade = input("Digite o nome da sua cidade: ")

dividir = cidade.split()
if "Santo" or "SANTO" or "santo" in dividir[0]:

    print("Sua cidade começa com a palavra 'Santo'")

else:
    print("Sua cidade não começa com a palavra 'Santo'")
