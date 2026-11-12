tocha = 30
while tocha > 0:
    caminho = input("___ O QUE VOCÊ ENCONTROU NO CAMINHO?? O TÃO ESPERADO TESOURO OU A ARMADILHA?? ___")

    tocha = tocha - 10
    
    if caminho == "tesouro":
        print ("___ VOCÊ PEGOU AS MOEDAS!! ___") 

    else:
        print ("___ VOCÊ DESVIOU DO PERIGO!! ___")



print ("___ A TOCHA APAGOU!! FIM DA EXPLORAÇÃO!! ___")