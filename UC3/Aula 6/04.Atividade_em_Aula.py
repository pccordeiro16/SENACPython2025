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

    def __str__(self):
        return f'--- {self.nome} é um {self.especie} {self.sexo} da raça {self.raca}. Come {self.alimento} e faz "{self.grunhido}"!\n'

    @abstractmethod
    def grunhir(self):
        pass

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def dormir(self):
        pass


class Cachorro(Animal):
    def __init__(self, nome, especie, alimento, grunhido, raca, sexo):
        super().__init__(nome, especie, alimento, grunhido)
        self.raca = raca
        self.sexo = sexo

    def grunhir(self):
        print(f'- {self.nome}: {self.grunhido.title()}!\n')

    def comer(self):
        print(f'- {self.nome} está comendo {self.alimento}.\n')

    def dormir(self):
        print(f'- {self.nome} foi dormir.\n')

    def buscar_bola(self):
        print(f'- {self.nome} foi correndo buscar a bola!')


class Gato(Animal):
    def __init__(self, nome, especie, alimento, grunhido, raca, sexo):
        super().__init__(nome, especie, alimento, grunhido)
        self.raca = raca
        self.sexo = sexo

    def grunhir(self):
        print(f'- {self.nome}: {self.grunhido.title()}!\n')

    def comer(self):
        print(f'- {self.nome} está comendo {self.alimento}.\n')

    def dormir(self):
        print(f'- {self.nome} foi tirar uma soneca.\n')

    def arranhar(self):
        print(f'- {self.nome} está arranhando o sofá!')

# Testando

dog1 = Cachorro('Zozo', 'cachorro', 'ração', 'au au', 'Shih Tzu', 'fêmea')
cat1 = Gato('Tom', "gato", "sachê", "miau", "Azul Russo", "macho")

print(dog1)
print(cat1)

print('\n----------------------------------------------------------------------\n')

dog1.grunhir()
dog1.comer()
dog1.dormir()
dog1.buscar_bola()

print('\n----------------------------------------------------------------------\n')

cat1.grunhir()
cat1.comer()
cat1.dormir()
cat1.arranhar()

# 3

class UsuarioRepository:
    def __init__(self):
        self.usuarios = []

    def cadastrar(self, usuario):
        self.usuarios.append(usuario)

    def listar_todos(self):
        return self.usuarios

    def buscar_por_email(self, email):
        for usuario in self.usuarios:
            if usuario["email"] == email:
                return usuario
        return None

    def remover(self, email):
        self.usuarios = [u for u in self.usuarios if u["email"] != email]

    def atualizar(self, usuario):
        for i, u in enumerate(self.usuarios):
            if u["email"] == usuario["email"]:
                self.usuarios[i] = usuario
                break

    def listar_por_nome(self, nome):
        return [u for u in self.usuarios if u["nome"] == nome]

    def listar_por_email(self, email):
        return [u for u in self.usuarios if u["email"] == email]

    def listar_por_nome_e_email(self, nome, email):
        return [u for u in self.usuarios if u["nome"] == nome and u["email"] == email]