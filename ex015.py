'''Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias no 
qual ele ficou alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado'''

dias = int(input("Digite quantos dias voce ficou com o carro: "))
km = float(input("Digite a quantidade de KMs percorridos: "))
pagar = (dias*60) + (0.15*km)
print(f"O total a pagar pelo carro é R$ {pagar:.2f} !")
