# Atividade Prática: Sistema de uma Biblioteca
'''
Contexto:
Você foi contratado para desenvolver um sistema de gerenciamento de biblioteca usando POO em Python.
O sistema deve modelar livros, usuários e empréstimos, com funcionalidades básicas de cadastro, consulta e operações.

Requisitos:
- O sistema deve permitir o cadastro de livros, usuários e empréstimos.
- O sistema deve permitir a consulta de livros cadastrados.
- O sistema deve permitir a consulta de usuários cadastrados.
'''

# DESAFIO (opcional) Classe LivroDigital:
# Herde de Livro e adicione o formato do e-book e formas de download.

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f'| {self.titulo} ({self.autor} - {self.ano}) |'
    
class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano, formato, link_download):
        super().__init__(titulo, autor, ano)
        self.formato = formato
        self.link_download = link_download

    def __str__(self):
        return f'| {self.titulo} (Digital - {self.formato}) | Download: {self.link_download} |'
    
class Usuario:
    def __init__(self, id, nome, cpf):
        self.id = id
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f'| ID: {self.id} | Nome: {self.nome} | CPF: {self.cpf} |'
    

from datetime import datetime

class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        self.data = datetime.now().strftime('%d/%m/%Y')
        self.hora = datetime.now().strftime('%H:%M')

    def __str__(self):
        return f'--- {self.usuario.nome} pegou o livro "{self.livro.titulo}" no dia {self.data}, às {self.hora}.\n'
    
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

    def cadastrarLivro(self, livro):
        self.livros.append(livro)

    def cadastrarUsuario(self, usuario):
        self.usuarios.append(usuario)

    def emprestarLivro(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def listarLivros(self):
        for livro in self.livros:
            print(livro)

    def listarUsuarios(self):
        for usuario in self.usuarios:
            print(usuario)

    def listarEmprestimos(self):
        for emprestimo in self.emprestimos:
            print(emprestimo)

mlib = Biblioteca()

book1 = Livro('One Piece Vol. 111', 'Eiichiro Oda', 2025)
book2 = Livro('Dom Casmurro', 'Machado de Assis', 1900)
mlib.cadastrarLivro(book1)
mlib.cadastrarLivro(book2)

user1 = Usuario(900, 'Joaquim da Silva', 12345678901)
user2 = Usuario(901, 'Kaio Vianna', 97865432110)
mlib.cadastrarUsuario(user1)
mlib.cadastrarUsuario(user2)

emp1 = Emprestimo(book1, user1)
emp2 = Emprestimo(book2, user2)
mlib.emprestarLivro(emp1)
mlib.emprestarLivro(emp2)

print('Livros:\n')
mlib.listarLivros()

print('\n----------------------------------------------------------------------\n')

print('Clientes:\n')
mlib.listarUsuarios()

print('\n----------------------------------------------------------------------\n')

print('Empréstimos realizados:\n')
mlib.listarEmprestimos()