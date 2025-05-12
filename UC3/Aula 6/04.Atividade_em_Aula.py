# Atividades Práticas:

# 1. Crie uma classe Conta com:
'''
Atributo _saldo (privado).
Getter saldo que retorna o valor formatado (ex: R$1000.00).
Setter que bloqueia valores negativos.
'''

# 2. Classes Abstratas:
'''
Crie uma classe abstrata Animal com método comum a todas as classes-filhas.
Implemente, pelo menos, as classes Cachorro e Gato com 3 métodos para cada uma.
'''

# 3. Padrão de Acesso a Repositórios

# Crie uma classe UsuarioRepository com os seguintes métodos:
'''
- cadastrar(usuario): cadastra um usuário (dicionário com nome e email).
- listar_todos(): retorna uma lista com todos os usuários cadastrados.
- buscar_por_email(email): retorna o usuário correspondente ao email informado.
- remover(email): remove o usuário correspondente ao email informado. 
- atualizar(usuario): atualiza os dados do usuário correspondente ao email informado.
- listar_por_nome(nome): retorna uma lista com todos os usuários que possuem o nome informado.
- listar_por_email(email): retorna uma lista com todos os usuários que possuem o email informado.
- listar_por_nome_e_email(nome, email): retorna uma lista com todos os usuários que possuem o nome e email informados.
'''

# 4. DESAFIO: retorne às atividades 2 e 3 e implemente uma metaclasse dentro de seus respectivos contextos.


#1 

class ContaBancaria:
    # Construtor da classe Conta Bancaria
    def __init__(self, nome, saldo):
        self._nome = nome
        self._saldo = None
        self.saldo = saldo

    # Getter para saldo:
    @property
    def saldo(self):
        return f'R${self._saldo:.2f}'
    
    # Setter para saldo:
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError('Saldo inválido. Insira um valor acima de R$0.00.')
        self._saldo = valor

    # Getter para nome:
    @property
    def nome(self):
        return self._nome.title()  # Retorna com primeira letra maiúscula

    # Setter para nome:
    @nome.setter
    def nome(self, valor):
        if len(valor) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres.")
        self._nome = valor

# exemplo:
user1 = ContaBancaria('Pedro Cordeiro', 25.985)
print(user1.saldo)
print(user1.nome)

#2

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, especie, alimento, grunhido):
        self.nome = nome
        self.especie = especie
        self.alimento = alimento
        self.grunhido = grunhido
        self.animais = []

    def __str__(self):
        return f'{self.nome} é um {self.especie} {self.sexo} da raça {self.raca}. Se alimento de {self.alimento} e faz: {self.grunhido}!'

    @abstractmethod
    def grunhir(self):
        pass

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def dormir(self):
        pass

    def novoAnimal(self, animal):
        self.animais.append(animal)

    def descreverAnimal(self):
        for animal in self.animais:
            print(animal)


class Cachorro(Animal):
    def __init__(self, nome, especie, alimento, grunhido, raca, sexo):
        super().__init__(nome, especie, alimento, grunhido)
        self.raca = raca
        self.sexo = sexo

    def grunhir(self):
        print(f'{self.nome}: {self.grunhido.title()}')

    def comer(self):
        print(f'{self.nome} está comendo {self.alimento}.')

    def dormir(self):
        print(f'{self.nome} foi dormir.')

    def buscar_bola(self):
        print(f'{self.nome} foi correndo buscar a bola!')


class Gato(Animal):
    def __init__(self, nome, especie, alimento, grunhido, raca, sexo):
        super().__init__(nome, especie, alimento, grunhido)
        self.raca = raca
        self.sexo = sexo

    def grunhir(self):
        print(f'{self.nome}: {self.grunhido.title()}!')

    def comer(self):
        print(f'{self.nome} está comendo {self.alimento}.')

    def dormir(self):
        print(f'{self.nome} foi tirar uma soneca.')

    def arranhar(self):
        print(f'{self.nome} está arranhando o sofá!')


# Testando
dog1 = Cachorro('Zozo', 'cachorro', 'ração', 'au au', 'Shih Tzu', 'fêmea')
cat1 = Gato('Tom', "gato", "sachê", "miau", "Azul Russo", "macho")

dog1.descreverAnimal()

dog1.grunhir()
dog1.comer()
dog1.dormir()
dog1.buscar_bola()

print('---')

cat1.grunhir()
cat1.comer()
cat1.dormir()
cat1.arranhar()
