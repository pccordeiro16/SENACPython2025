########################################
#      AULA 05 - 10.03.2025          ##
######################################

# ATIVIDADE 01

preco = 150
desconto = 20
print('O preço final é ', preco - desconto)
 
# ATIVIDADE 02

peso = 70
altura = 1.75
imc = (peso / (altura ** 2))
print('O Índice de Massa Corporal é igual a {}!'.format(imc))

# ATIVIDADE 03

idade = 22
tem_exp = True
concurso_eleg = idade >= 18 and tem_exp
print('Essa pessoa é elegível para o concurso?')
if concurso_eleg:
    print('Sim!')
else:
    print('Não!')

# ATIVIDADE 04

nivel_acesso = int(input('Digite seu nível de acesso:'))
if nivel_acesso == 3:
    print('Acesso total!')
elif nivel_acesso == 2:
    print('Acesso parcial!')
elif nivel_acesso == 2:
    print('Acesso restrito!')
else:
    print('Erro. Digite um número válido!')

# ATIVIDADE 05

c = float(input('Qual a temperatura, em ºC, no momento?'))
f = (((c * 9) / 5) + 32)
print('A temperatura marca {}ºC ou {}ºF!'.format(c, f))

# ATIVIDADE 06

num = int(input('Digite um número:'))
par = (num % 2)
if par == 0:
    print(num,': Este é um número par!')
else:
    print(num,': Este é um número ímpar!')

# ATIVIDADE 07

peso = int(input('Quanto pesa o pacote em kg?'))
if peso <= 5:
    print('Para {}kg, frete: R$10,00'.format(peso))
elif 5 < peso <= 10:
    print('Para {}kg, frete: R$20,00'.format(peso))
elif peso > 10:
    print('Para {}kg, frete: R$30,00'.format(peso))
