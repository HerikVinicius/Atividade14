print("Calculador de aumento")
salario = float(input("Digite o valor do seu salário atual: "))
if salario > 1250:
    print(f"O seu salário agora será de {salario+(salario*(10/100))}")
else:
    print(f"O seu salário agora será de {salario+(salario*(15/100))}")