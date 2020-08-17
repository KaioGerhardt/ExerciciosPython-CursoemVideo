# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input("Digite o valor do produto em R$ "))
d = (preco * 5)/100
nvpreco = preco - d
print(f"O preço do produto era de R$ {preco:.2f}, com um desconto de 5% passou a ficar R$ {nvpreco:.2f}!")