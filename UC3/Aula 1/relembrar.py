# ATIVIDADE 01
# Cálculo de Média de Notas: Peça ao usuário que insira 4 notas (de 0 a 10).
# Calcule a média das notas e exiba o resultado. Se a média for maior ou igual a 7, exiba "Aprovado".
# Caso contrário, exiba "Reprovado".

notas = []

for i in range(1, 5):
    nota = float(input(f'Digite a nota {i} (de 0 a 10): '))
    while nota < 0 or nota > 10:
        print('Nota inválida. Digite um valor entre 0 e 10')
        nota = float(input(f'Digite a nota {i} (de 0 a 10): '))
    notas.append(nota)

media = sum(notas) / 4

print(f'Média: {media:.2f}')
if media >= 7:
    print('Aprovado!')
else:
    print('Reprovado!')

# 2. Soma dos Números Pares em um Intervalo:
# Peça ao usuário dois números, representando o início e o fim de um intervalo.
# Use um loop (for ou while) para calcular a soma de todos os números pares nesse intervalo e exiba o resultado.
