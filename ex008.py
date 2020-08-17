# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
 
metros = float(input("Digite um valor em metros: "))
mm = metros *1000
cm = metros * 100

print(f"{metros:.2f} metros são {cm:.2f}cm e {mm:.2f}mm!")