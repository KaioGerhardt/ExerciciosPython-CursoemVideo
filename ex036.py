''' Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. Pergunte o valor da casa, o salario
do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salario ou então o emprestimo
será negado '''

vcasa = float(input("Digite o valor da casa em R$ "))
salario = float(input("Digite o seu salário em R$ "))
anos = int(input("Digite em quantos anos pretende pagar a casa: "))
prest = vcasa / (anos * 12)
print(prest)