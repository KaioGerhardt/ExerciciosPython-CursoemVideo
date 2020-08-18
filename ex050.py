''' Desenvolva um programa que leis seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor 
digitado for impar, desconsidere-o. '''

s = 0
for c in range(1, 7):
    d = int(input("Digite um numero: "))
    if c % 2 == 0:
        s = d + s
print(s)