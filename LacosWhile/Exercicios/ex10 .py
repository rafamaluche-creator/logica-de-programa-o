energia = 30 

while energia > 0:
    minerio = input("___QUE MINERIO VOCÊ ENCONTROU??___")
    minerio = minerio.lower()
    
    if minerio == "ouro":
        print ("___BOM TRABALHO!!___")

        energia = energia - 10

    print ("___VOCÊ ESTÁ MAIS CANÇADO COM APENAS", energia , "... MAS TRABALHE CONDENADO___")

else:
    print("___VOCÊ FICOU COM PREGUIÇA E FOI PRA CASA___")

