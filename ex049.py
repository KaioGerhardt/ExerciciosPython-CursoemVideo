''' Refazer o mesmo desfio 009, mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando
o laço for. '''

n = int(input("Digite um valor para saber sua tabuada: "))

for c in range(1, 11):
    print(f"{n} X {c} = {n*c}")