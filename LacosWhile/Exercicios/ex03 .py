op = "0"

while op != "3":
    print("________________________")
    print("___BEM VINDO AO JOGO___")
    print("___MENU___")
    print("1. JOGAR")
    print("2. VER INVENTÁRIO")
    print("3. SAIR DO JOGO")
    print("________________________")

    op = input("OQUE VOCÊ DESEJA FAZER: ")

    if op == "1":
        print("\n___CARREGANDO O MAPA___")
    elif op == "2":
        print("\n___VERIFICANDO INVENTÁRIO___")
    elif op == "3":
        print("\n___ATÉ MAIS___")
    else:
        print("\n___TENTE NOVAMENTE___")       
