preco = float(input("Digite o preço: "))

if preco <= 100:
    print("5% desconto")
elif preco >= 100.1 and preco <= 300:
    print("10% desconto")
elif preco >= 300:
    print("15% desconto")