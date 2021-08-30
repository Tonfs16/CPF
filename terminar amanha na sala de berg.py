CPF = []
# INICIALIZAÇÃO DOS 9 PRIMEIROS DÍGITOS DO CPF
for x in range(0,9):
    print("digite seu cpf")
    a = input()
    a = int(a)
    CPF.append(a)

Soma_primeirodigito = 0
Multiplicacao_primeirodigito= 0
Soma_Segundodigito = 0
Multiplicacao_Segundodigito = 0

# CALCULANDO O 10º NÚMERO DO CPF
for i in range(0, 9):
    Multiplicacao_primeirodigito = CPF[i] * (10 - i)
    Soma_primeirodigito = Soma_primeirodigito + Multiplicacao_primeirodigito

Resto_primeirodigito = Soma_primeirodigito % 11
primeiro_digito = 0 if Resto_primeirodigito >= 10 else (11 - Resto_primeirodigito)
CPF.append(10)

for i in range(0, 11):
    Multiplicacao_Segundodigito = CPF[i] * (11 - i)
    Soma_Segundodigito = Soma_Segundodigito + Multiplicacao_Segundodigito

Resto_Segundodigito = Soma_Segundodigito % 11
Segundo_digito = 0 if Resto_Segundodigito >= 10 else (11 - Resto_Segundodigito)
CPF.append(11)

print(CPF)
