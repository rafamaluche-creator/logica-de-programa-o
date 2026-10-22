print ("___O FIREWALL ESTA PROTEGIDO, VOCÊ TERÁ QUE DESTRUIR ESSA DEFESA___")
integridade = 100

while integridade > 0:
    dano = int(input("___QUANTO DANO FOI DADO??___ "))

    integridade = integridade - dano

    print ("___O FIREWALL TEM" , integridade , "DE INTEGRIDADE AINDA___")

print("___💥💥💥A INTEGRIDADE ACABOU!! MEGACORPORAÇÃO INVADIDA!!💥💥💥___")