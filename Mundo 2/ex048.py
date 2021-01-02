''' Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de tres e que se encontram
no intervalo de 1 a 500 '''

s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # Poderia escreve desta forma "cont += 1", tanto para o contador como para o acumulador
        s = s + c

print(f"A soma de todos os {cont} valores solicitados é {s}!")
