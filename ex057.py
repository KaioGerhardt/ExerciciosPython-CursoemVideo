''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a 
digitação novamente até ter um valor correto. '''

#s = "F" or "M"
s = str()
while (s = "F" or "M"):
    s = str(input("Favor informe seu sexo: [F/M] ")).upper
    if s != "M" or "F":
        print("Favor insira uma resposta válida! ")
    else:
        print("Obrigado, resposta válida! ")


        #ARRUMAR