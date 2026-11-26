def retangulo (largura, altura):
    for x in range(altura):
        print(":" * largura)

retangulo (5, 2)

def quadrado(lado):
    retangulo(lado, lado)

quadrado(4)