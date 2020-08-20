# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis 
# sobre ela.

a = input("Digite qualquer coisa: ")
print("Qual é o seu tipo primitivo? ", type(a)) #Função utilizada para descobrir o tipo primitivo
print("É apenas espaços? ", a.isspace()) # Utilizado para saber se possui apenas espaços 
print("São letras e numeros? " a.isalnum())