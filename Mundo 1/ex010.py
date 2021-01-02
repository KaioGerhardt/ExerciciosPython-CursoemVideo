'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.

Considere U$ 1,00 = R$ 3,27
'''

din = float(input("Quanto de dinheiro voce tem na carteira em R$? "))
dol = din / 3.27

print(f"Com R$ {din:.2f} voce tem U$ {dol:.2f} !")