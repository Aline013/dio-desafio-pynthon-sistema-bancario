menu = """
Escolha uma opção

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
              saldo += valor
              extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("\n===================================")
            print("Operação falhou! O valor informado é inválido.")
            print("===================================")

    elif opcao == "s":
          valor = float(input("Informe o valor do saque:"))

          excedeu_saldo = valor > saldo

          excedeu_limite = valor > limite

          excedeu_saques = numero_saques >= limite_saques

          if excedeu_saldo:
              print("\n===================================")
              print("Operação falhou! Você não tem saldo suficiente.")
              print("===================================")

          elif excedeu_limite:
              print("\n===================================")
              print("Operação falhou! Valor superior ao limite permitido por saque.")
              print("===================================")

          elif excedeu_saques:
              print("\n===================================")
              print("Operação falhou! Você excedeu o limite de saques diários.")
              print("===================================")

          elif valor > 0:
              saldo -= valor
              extrato += f"Saque: R$ {valor:.2f}\n"
              numero_saques += 1

          else:
              print("\n===================================")
              print("Operação falhou! O valor informado é inválido.")
              print("===================================")

    elif opcao == "e":
          print("\n==============EXTRATO==============\n")
          print("Não foram realizadas movimentações.\n" if not extrato else extrato)
          print(f"Saldo: R$ {saldo:.2f}")
          print("\n===================================")

    elif opcao == "q":
        break

    else:
        print("\n===================================")
        print("Operação inválida! Por favor, selecione novamente a operação desejada.")
        print("===================================")
