n = float(input("Digite sua nota (0 a 10): "))

if 0 <= n <= 4:
    print("Reprovado")
elif 4 < n <= 6:
    print("Exame")
elif 6 < n <= 10:
    print("Aprovado")
else:
    print("Nota inválida")


   
