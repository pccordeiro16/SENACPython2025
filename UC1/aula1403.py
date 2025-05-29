# 1. Contagem Regressiva com FOR:
#Peça ao usuário um número e faça uma contagem regressiva a partir dele até 0.

numero = int(input('Digite um número para a contagem regressiva'))
for i in range (numero, -1, -1):
    print(i)


# 2. Soma de Números com WHILE:
# Peça ao usuário um número e some
# Todos os números de 1 até ele.

numero = int(input('Digite um número para somar de 1 até ele'))
soma = 0
i = 1
while i <= numero:
    soma += i
    i += 1
print('Soma:', soma)


# 3. Tabuada com FOR:
# Peça ao usuário um número e mostre a tabuada dele de 1 a 10.

numero = int(input('Digite um número para ver sua tabuada de 1 a 10'))
for i in range (1, 11):
    print(f'{numero} x {i} = {numero * i}')

# 4. Números Pares com FOR:
# Peça ao usuário um número e mostre todos os números pares de 1 até ele.
    
numero = int(input('Digite um número'))
cert = numero + 1
for i in range(0, cert, 2):
    print(i)

# 5. Fatorial com WHILE:
# Peça ao usuário um número e calcule o fatorial dele.

numero = int(input('Digite um número para calular seu fatorial:'))
fatorial = 1
i = 1
while i <= numero:
    fatorial *= i
    i += 1
print(f'{numero}! = {fatorial}')

# 6. Validação de Entrada com WHILE:
# Peça ao usuário um número maior que 10. Se ele digitar um número inválido, peça novamente.

numero = 0
while numero <= 10:
    numero = int(input('Digite um número maior que 10:'))
print('Número válido:', numero)

