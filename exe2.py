idade = int(input("Digite sua idade: "))

if idade <= 12 and idade <= 0:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolecente")
elif idade >= 18:
    print("Adulto")
else: 
    print("Idade invalida")
