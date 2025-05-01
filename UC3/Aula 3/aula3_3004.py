#Listas (Mutáveis, ordenadas, aceitam duplicatas)

# Criando e acessando sua lista:
lista_teste = [10, 20, 30, 40]
print(lista_teste[1])  # Saída: 20 (indexação começa em 0)
print(lista_teste[1:3])  # Saída: [20, 30] (fatiamento)
print(lista_teste[-1])  # Saída: 40 (último elemento)
print(lista_teste[-2:])  # Saída: [30, 40] (últimos dois elementos)
print(lista_teste[:2])  # Saída: [10, 20] (primeiros dois elementos) 
print(lista_teste[::2])  # Saída: [10, 30] (elementos em posições pares)
print(lista_teste[::-1])  # Saída: [40, 30, 20, 10] (inversão da lista)   
print(lista_teste[1:4:2])  # Saída: [20, 40] (fatiamento com passo 2)
print(lista_teste[1:])  # Saída: [20, 30, 40] (do índice 1 até o final) 
print(lista_teste[:3])  # Saída: [10, 20, 30] (do início até o índice 2)
print(lista_teste[-3:-1])  # Saída: [20, 30] (do índice -3 até -2)        
print(len(lista_teste))  # Saída: 4 
print(lista_teste.count(20))  # Saída: 1 (conta quantas vezes o valor 20 aparece na lista)

# Métodos essenciais:
lista_teste.append(50)        # Adiciona no final: [10, 20, 30, 40, 50]
print(lista_teste)
lista_teste.insert(1, 15)     # Insere na posição 1: [10, 15, 20, 30, 40, 50]
print(lista_teste)
lista_teste.remove(20)        # Remove o valor 20: [10, 15, 30, 40, 50]
print(lista_teste)
valor = lista_teste.pop(2)    # Remove e retorna o índice 2 (30): [10, 15, 40, 50]
print(lista_teste)
lista_teste.sort()            # Ordena em ordem crescente/alfabética: [10, 15, 40, 50]
print(lista_teste)
lista_teste.reverse()         # Inverte a ordem: [50, 40, 15, 10]
print(lista_teste)
lista_teste.clear()          # Limpa a lista: []
print(lista_teste)

####################################################################################################################################################################################################

#Tuplas (Imutáveis, ordenadas, aceitam duplicatas)

# Criando e acessando:
tupla_teste = (1, 2, 3, 2)
print(tupla_teste.count(2))   # Conta ocorrências de 2 → 2
print(tupla_teste.index(3))   # Retorna o índice do valor 3 → 2

# Conversão para lista (útil para modificações):
lista_modificavel = list(tupla_teste)

# Criando uma tupla de departamentos:
departamentos = ("RH", "TI", "Vendas")

# Acessando um elemento:
print(departamentos[1])  # Saída: "TI"

departamentos.append("Marketing")  # Adicionaria no final, a princípio: ("RH", "TI", "Vendas", "Marketing") porém, isso não é possível, pois tuplas são imutáveis.
# Tentativa de modificação (erro)!!!!
# departamentos recebendo o elemento "Marketing"  # AttributeError!!!!

####################################################################################################################################################################################################

#Dicionários (Pares chave-valor, mutáveis)

# Criando e manipulando:
dados = {"id": 1, "nome": "Ana", "cargo": "Dev"}
print(dados.get("nome", "endereço"))  # Saída: Ana

# Métodos úteis:
dados.update({"salario": 7000})
print(dados)                         # Adiciona/atualiza chaves → {"id": 1, "nome": "Ana", "cargo": "Dev", "salario": 7000}
cargo = dados.pop("cargo")           # Remove e retorna o valor → cargo = "Dev"
print(dados)                         
print(dados.keys())                  # Retorna todas as chaves → dict_keys(['id', 'nome', 'salario'])
print(list(dados.values()))          # Valores como lista → [1, 'Ana', 7000]

# Criando um dicionário de colaboradores:
colaborador = {
    "id": 101,
    "nome": "Ana Silva",
    "cargo": "Desenvolvedora Back-End"
}

# Adicionando um novo campo:
colaborador["salario"] = 7500.00

# Acessando um valor:
print(colaborador["nome"])  # Saída: "Ana Silva"

# Removendo um campo:
del colaborador["cargo"]    # Remove o campo "cargo"

# Iterando um dicionário:
for chave, valor in colaborador.items():
    print(f"{chave}: {valor}")  # Saída: id: 101, nome: Ana Silva, salario: 7500.0

# Copiando um dicionário:
novo_colaborador = colaborador.copy()   # Cria uma cópia do dicionário colaborador
print(novo_colaborador)  # Saída: {'id': 101, 'nome': 'Ana Silva', 'salario': 7500.0}   

# Limpar um dicionário:
colaborador.clear()  # Limpa o dicionário → {}
print(colaborador)  # Saída: {}

# Criando um dicionário com compreensão de dicionário:
dicionario_compreensao = {x: x**2 for x in range(5)}  # Cria um dicionário com chaves de 0 a 4 e valores quadrados
print(dicionario_compreensao)  # Saída: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}     

# Criando um dicionário com dicionário aninhado:
dicionario_aninhado = {
    "pessoa1": {
        "nome": "Ana",
        "idade": 25
    },
    "pessoa2": {
        "nome": "João",
        "idade": 30
    }
}       

print(dicionario_aninhado)

####################################################################################################################################################################################################

#Sets (Mutáveis, não ordenados, únicos)

# Criando e operações:
conjunto = {1, 2, 3, 4, 4}  # Remove duplicatas → {1, 2, 3, 4}
print(conjunto)              # Saída: {1, 2, 3, 4}
conjunto.add(5)              # Adiciona valor → {1, 2, 3, 4, 5}
print(conjunto)
conjunto.discard(2)          # Remove se existir → {1, 3, 4, 5}
print(conjunto)

# Operações matemáticas:
outro_conjunto = {3, 4, 5, 6}
print(conjunto.union(outro_conjunto))           # União → {1, 3, 4, 5, 6}
print(conjunto.intersection(outro_conjunto))    # Interseção → {3, 4, 5}

conjunto.difference_update(outro_conjunto)  # Diferença → {1}
print(conjunto)  # Saída: {1}

conjunto.clear()  # Limpa o conjunto → set()
print(conjunto)