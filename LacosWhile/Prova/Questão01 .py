print ("___ O CANHÃO ESTA SEM CARGA ___")
carga = 0

while carga < 100:
    energia = int(input("___ QUANTO DE ENERGIA DESEJA INJETAR??___"))

    carga = carga + energia

print ("___ CANHÃO COMPLETAMENTE CARREGADO! FOGO! ___")