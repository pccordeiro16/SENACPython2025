# Importa o módulo math, que fornece funções matemáticas, como raiz quadrada e funções trigonométricas
import math

# Define a função principal da calculadora
def calculadora():
    # Dicionário que mapeia operações matemáticas para funções lambda (funções anônimas)
    operacoes = {
        '+': lambda x, y: x + y,                       # Soma
        '-': lambda x, y: x - y,                       # Subtração
        '*': lambda x, y: x * y,                       # Multiplicação
        '/': lambda x, y: x / y,                       # Divisão
        '^': lambda x, y: x ** y,                      # Potência (x elevado a y)
        '√': lambda x: math.sqrt(x),                   # Raiz quadrada
        'sen': lambda x: math.sin(math.radians(x)),    # Seno, convertendo graus para radianos
        'cos': lambda x: math.cos(math.radians(x)),    # Cosseno
        'tan': lambda x: math.tan(math.radians(x))     # Tangente
    }
    
    # Loop principal que mantém a calculadora funcionando até o usuário digitar 'sair'
    while True:
        # Mostra as operações disponíveis
        print("\nOperações disponíveis:")
        print("+, -, *, /, ^ (potência), √ (raiz), sen, cos, tan")
        print("Digite 'sair' para encerrar")
        
        # Solicita ao usuário que informe a operação desejada
        op = input("Operação: ")
        
        # Se o usuário digitar 'sair', o loop é interrompido
        if op.lower() == 'sair':
            break
        
        # Se a operação for unária (apenas um número), como raiz ou trigonometria
        if op in ['√', 'sen', 'cos', 'tan']:
            num = float(input("Número: "))  # Solicita o número ao usuário
            try:
                resultado = operacoes[op](num)  # Executa a operação usando o dicionário
                print(f"Resultado: {resultado:.4f}")  # Mostra o resultado com 4 casas decimais
            except ValueError as e:
                print(f"Erro: {e}")  # Trata erros como raiz de número negativo
        # Se for uma operação binária (dois números), como soma ou potência
        elif op in operacoes:
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))
            try:
                resultado = operacoes[op](num1, num2)  # Executa a operação
                print(f"Resultado: {resultado:.4f}")
            except ZeroDivisionError:
                print("Erro: Divisão por zero!")  # Trata erro específico de divisão por zero
            except Exception as e:
                print(f"Erro: {e}")  # Trata qualquer outro erro
        else:
            print("Operação inválida!")  # Caso a operação digitada não exista

# Chama a função calculadora para iniciar o programa
calculadora()
