saldo = 100
op = "0"

print("________________________________")
print("____!!BEM VINDO A PADARIA!!_____")

while op != "3":
    print("________________________________")
    print("__OQUE VOCÊ DESEJA COMPRAR?__")
    print("________________________________")
    print("\n _SEU SALDO É DE: R$", saldo)
    print("1 - PÃO__ R$ 1,00")
    print("2 - BOLO__ R$ 10,00")
    print("________________________________")
    print("0 - SAIR")
    op = input("__ESCOLHA UMA OPÇÃO: ")

    if op == "1":
        if saldo >= 1:
            saldo -= 1
            print("________________________________")
            print("VOCÊ COMPROU UM PÃO!")
            print("SEU SALDO AGORA É DE: R$", saldo)
        else:
            print("________________________________")
            print("SALDO INSUFICIENTE PARA COMPRAR UM PÃO!")
    elif op == "2":
        
        if saldo >= 10:
            saldo -= 10
            print("________________________________")
            print("VOCÊ COMPROU UM BOLO!")
            print("SEU SALDO AGORA É DE: R$", saldo)
        else:
            print("________________________________")
            print("SALDO INSUFICIENTE PARA COMPRAR UM BOLO!")
    else:
        print("________________________________")
        print("OPÇÃO INVÁLIDA!!")
        print("________________________________")
        print("VOLTE SEMPRE!!")
        