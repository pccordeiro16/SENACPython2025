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
        return f'{self.titulo} ({self.autor} - {self.ano})'
    
class Usuario:
    def __init__(self, id, nome, cpf):
        self.id = id
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f'| ID: {self.id} | Nome: {self.nome} | CPF: {self.cpf} |'
    
class Emprestimo:
    def __init__(self, livro, usuario, data, hora):
        self.livro = livro
        self.usuario = usuario
        self.data = data
        self.hora = hora

    def __str__(self):
        return f'{self.usuario.nome} pegou o livro "{self.livro.titulo}" no dia {self.data}, às {self.hora}.'
    
class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano, formato, link_download):
        super().__init__(titulo, autor, ano)
        self.formato = formato
        self.link_download = link_download

    def __str__(self):
        return f'{self.titulo} (Digital - {self.formato}) - Download: {self.link_download}'