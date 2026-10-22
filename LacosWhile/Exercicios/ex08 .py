print ("___VOCÊ CHEGOU EM UMA BIFURCAÇÃO___")
lado = input ("___PARA QUAL LADO VOCÊ VAI??___")

if lado == "esquerda":
    print ("___!!HÁ UM GOBLIN A FRENTE!!___")

    ação = input ("___VOCÊ VAI ATACAR OU FUGIR??___")
    if ação == "atacar":
        print ("___VOCÊ AMASSOU O MONSTRO___")

    else:
        print ("___VOCÊ FUGIU BEM, CAGÃO___")

if lado == "direita":
    print ("___VOCÊ ACHOU UM BAÚ___")

    bau = input ("___DESEJA ABRIR OU IGNORAR ELE??___")
    if bau == "abrir":
        print ("___ERA UMA ARMADILHA, ACABOU PRA VOCÊ___")

    else:
        print ("___PASSOU DIRETO... CONTINUE SUA JORNADA___")
elif lado == "voltar":
    print ("___VOCÊ VOLTA PARA CASA, MAS ELA FOI ESMAGADA POR UM TITÃ COM VOCÊ DENTRO___")

else:
    print ("___NÃO TEM ESSA OPÇÃO___")