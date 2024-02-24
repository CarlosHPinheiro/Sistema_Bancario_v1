saldo = 0
LIMITE = 500
saques_efetuados = 0
LIMITE_SAQUES = 3
extrato = ""

menu= """
===== MENU =====
      [D] Depósito
      [S] Saque
      [E] Extrato
      [Q] Sair 
"""

while True:
    opcao = input(menu).upper()
    if opcao == "D":
        print("Depósito")
        deposito = int(input("Valor do Depósito: "))

        if deposito <= 0 :
            print("Operação Inválida")

        else:
            saldo += deposito
            extrato += f"Depósito no valor de R${deposito:.2f}\n" 
            print(f"Depósito efetuado no valor de R${deposito:.2f}")

    elif opcao == "S":
        print("Saque")
        saque = int(input("Valor do Saque: "))

        if saques_efetuados == LIMITE_SAQUES:
            print("Limite diário de saques atingido!")

        elif saque > LIMITE:
            print("Valor acima do limite permitido!")

        elif saldo < saque:
            print("Saldo insuficiente!")
        
        else:
            saldo -= saque
            extrato += f"Saque no valor de R${saque:.2f}\n"
            saques_efetuados += 1
            print(f"Saque efetuado no valor de R${saque:.2f}")

    elif opcao == "E":
        print("===Extrato===\n")
        if not extrato:
            print("Não foram realizadas movimentações.")
            print(f"Saldo Atual: R${saldo:.2f}")
        else:
            print(f"{extrato} \nSaldo Atual: R${saldo:.2f}")

    elif opcao == "Q":
        print("Tenha um bom dia!")
        break

    else:
        print ("Opcão Inválida!")
