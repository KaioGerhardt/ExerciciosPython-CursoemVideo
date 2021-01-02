'''
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2 m².
'''

altura = float(input("Digite a altura da parede em metros: "))
largura = float(input("Digite a largura da parede em metros: "))

area = largura * altura
litros = area / 2

print(f"Com uma parede de {area}m² é necessario {litros} litros de tinta! ")
