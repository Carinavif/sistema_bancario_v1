menu = """ Menu de Atendimento

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Selecionada a opção de depósito.")
        valor = float(input("Informe um valor a ser depositado:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else: 
            print("Operação inválida, valor informado não existe, tente novamente.")


    elif opcao == "2":
        print("Selecionado opção de Saque.")
        valor = float(input("Insira um valor de saque:"))

        excedeu_valor = valor > saldo 
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_valor:
            print("Operação inválida, você não tem saldo o suficiente para esse saque, por favor digitar um novo valor:")

        elif excedeu_limite: 
            print(f"O valor máximo por saque é R${limite:2f} por favor tente novamente com um valor válido.")

        elif excedeu_saque:
            print(f"A quantidade máxima de saques feitos por dia são de {LIMITE_SAQUES}, por favor tente novamente amanhã. Caso você não tenha feito os 3 saques, entrar em contato com o seu gerente.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")


                       
    elif opcao == "3":
      print("Selecionado opção de exibir Extrato.")
      print("\n================ EXTRATO ================")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("==========================================")

      
      

    elif opcao == "0":
       print("Obrigada por escolher os nossos serviços, tenha um bom dia!")
       break

       
    else: 
        print("Operação Inválida, tente novamente.")
     


