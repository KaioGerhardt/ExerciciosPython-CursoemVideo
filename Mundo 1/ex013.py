# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

salario = float(input("Digite o salario do funcionario em R$ "))
reajuste = salario + ((salario*15)/100)
print(f"Com um reajuste de 15% o salario do funcionario passou de R$ {salario} para R$ {reajuste}!")
