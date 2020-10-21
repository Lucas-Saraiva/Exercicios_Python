altura = float(input("Qual a sua altura:"))
sexo = str(input("Qual é o seu sexo:[M] [F]")).upper()

if sexo == "F":
    pesoI = (62.1 * altura) - 44.7
    print(f"O seu peso ideal é {pesoI:.2f}")
elif sexo == "M":
    pesoI = (72.7 * altura) - 58
    print(f"O seu peso ideal é {pesoI:.2f}")
