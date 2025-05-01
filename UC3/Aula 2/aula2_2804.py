# Comentários de uma linha
'''
Comentários de múltiplas linhas (na verdade, são strings não atribuídas)
'''

# Exemplo de função básica
def saudacao(nome):
    return f'Olá, {nome}!'

print(saudacao('Maria')) # Saída: Olá, Maria!

# Tipos básico
inteiro = 42
flutuante = 3.1415
texto = 'Python'
booleano = True
complexo = 3 + 4j

# Tipos sequenciais
lista = [1, 2, 3, 'quatro']
tupla = (1, 2, 3) # Imutável
conjunto = {1, 2, 3} # Únicos e não ordenados
dicionario = {'nome': 'João', 'idade': 30}

# None representa a ausência de valor
nada = None

# Verificando tipos
print(type(texto)) # <class 'str'>
print(isinstance(flutuante, float)) # True

# Entrada básica
nome = input('Digite seu nome: ')
print(f'Bem-vindo, {nome}!')

# Convertendo tipos
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (em metros): "))

print(f"Você tem {idade} anos e {altura}m de altura.")

# Exemplo básico
nota = float(input('Digite sua nota(0-10): '))

if nota >= 0:
    conceito = 'A'
elif nota >= 7:
    conceito = 'B'
elif nota >= 5:
    conceito = 'C'
else:
    conceito = 'D'

print(f'Seu conceito é {conceito}')

# Operadores lógicos
idade = int(input('Digite sua idade: '))
tem_ingresso = input('Tem ingresso? (s/n): ').lower() == 's'

if idade >= 18 and tem_ingresso:
    print('Acesso permitido ao evento.')
elif idade >= 18 and tem_ingresso:
    print('Acesso permitido apenas com responsável.')
else:
    print('Acesso negado.')

# Operador ternário
status = 'Aprovado' if nota >= 5 else 'Reprovado'
print(status)

# 05 - Exemplos

def calcular_imc():
    peso = float(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altua (m): '))

    imc = peso / (altura ** 2)

    print(f'Seu IMC é {imc:.2f}')

    if imc < 18.5:
        print('Classificação: Magreza')
    elif imc < 25:
        print('Classificação: Normal')
    elif imc < 30:
        print('Classificação: Sobrepeso')
    elif imc < 40:
        print('Classificação: Obesidade')
    else:
        print('Classificação: Obesidade Grave')

calcular_imc()

def verificar_palindromo():
    texto = input("Digite uma palavra ou frase: ").lower().replace(" ", "")
    if texto == texto[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")

verificar_palindromo()

# Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja", "uva"]
for fruta in frutas:
    print(fruta.upper())

# Com enumerate para índice e valor
for indice, fruta in enumerate(frutas, start=1):
    print(f"{indice}. {fruta}")

# Range
for i in range(5):  # 0 a 4
    print(i)

for i in range(1, 11, 2):  # 1, 3, 5, 7, 9
    print(i)

# "List comprehension"
quadrados = [x**2 for x in range(10)]
print(quadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Exemplo básico

contador = 0
while contador < 5: 
    print(contador)
    contador += 1

# Loop com break e continue
while True:
    resposta = input("Digite 'sair' para terminar: ")
    if resposta.lower() == 'sair':
        break
    elif resposta == '':
        continue
    print(f"Você digitou: {resposta}")

# Exemplo: Adivinhe o número
import random
from random import randint
numero_secreto = random.randint(1, 100)
tentativas = 0
while True:
    tentativa = int(input("Adivinhe o número (1-100): "))
    tentativas += 1
    
    if tentativa < numero_secreto:
        print("Muito baixo!")
    elif tentativa > numero_secreto:
        print("Muito alto!")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break