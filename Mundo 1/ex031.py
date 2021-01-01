''' Desenvolva um programa que pergunte a distancia de uma viagem em KM. Calcule o preço da passagem, 
cobrando R$ 0,50 por KM para viagens de até 200km e R$ 0,45 para viagens mais longas. '''

d = float(input("Digite a distancia da viagem em KM "))
if d <= 200:
    print(f"Com {d}Km de distancia o preço da viagem fica R$ {d*0.5:.2f} ")
else:
    print(f"Com {d}Km de distancia o preço da viagem fica R$ {d*0.45:.2f} ")