ss = 0

while ss != 42:
    ss = int(input("___QUAL A SENHA?__"))

    if ss < 42:
        print("\n___MUITO BAIXO!___")

    elif ss > 42:
        print("\n___MUITO ALTO!___")

    else:
        print("\n___ACERTOU!___")
