# Faça um programa que leia um ano qualquer e mostres se ele é bissexto.

ano = int(input("Digite um ano para sabe se ele é bissexto: "))
if ano % 4 == 0:
    print(f"O ano de {ano} é BISSEXTO!")
else:
    print(f"O ano de {ano} NÂO é Bissexto!")