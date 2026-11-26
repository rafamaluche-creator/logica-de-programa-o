def calcular_total (preco, quantidade):
    return preco * quantidade 

total = calcular_total(12, 3)
print("o total da sua compra é ", total)

troco = 100 - calcular_total(12, 3)
print("seu troco de cem é ", troco)

print(calcular_total(6, 2) + calcular_total (3, 4))
