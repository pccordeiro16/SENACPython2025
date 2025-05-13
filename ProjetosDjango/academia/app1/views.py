from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
    <meta charset="UTF-8">
    <title>A Cademia</title>
    <style>
        body {
        font-family: Arial, sans-serif;
        background: #f2f2f2;
        margin: 0;
        padding: 0;
        }

        header {
        background-color: #222;
        color: #fff;
        padding: 20px;
        text-align: center;
        }

        nav {
        background-color: #444;
        padding: 10px;
        text-align: center;
        }

        nav a {
        color: white;
        text-decoration: none;
        margin: 0 15px;
        font-weight: bold;
        }

        .hero {
        background: url('https://images.unsplash.com/photo-1599059811896-09b3b27c7b3c') no-repeat center center;
        background-size: cover;
        color: white;
        padding: 100px 20px;
        text-align: center;
        }

        .hero h1 {
        font-size: 3em;
        margin: 0;
        }

        .conteudo {
        padding: 20px;
        text-align: center;
        }

        .rodape {
        background-color: #222;
        color: white;
        text-align: center;
        padding: 15px;
        margin-top: 40px;
        }
    </style>
    </head>
    <body>

    <header>
        <h1>Academia BananaFit</h1>
        <p>Fica forte ou fica fraco, você escolhe</p>
    </header>

    <nav>
        <a href="#">Início</a>
        <a href="#">Planos</a>
        <a href="#">Contato</a>
    </nav>

    <section class="hero">
        <h1>Treine com a gente</h1>
        <p>Músculo não se constrói no sofá</p>
    </section>

    <section class="conteudo">
        <h2>Planos a partir de R$49,90</h2>
        <p>Musculação, aeróbico, funcional e mais!</p>
    </section>

    <footer class="rodape">
        <p>© 2025 BananaFit. Todos os direitos reservados.</p>
    </footer>

    </body>
    </html>
    """
    return HttpResponse(html)

def end(request):
    html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
    <meta charset="UTF-8">
    <title>A Cademia</title>
    <style>
        body {
        font-family: Arial, sans-serif;
        background: #f2f2f2;
        margin: 0;
        padding: 0;
        }

        header {
        background-color: #222;
        color: #fff;
        padding: 20px;
        text-align: center;
        }

        nav {
        background-color: #444;
        padding: 10px;
        text-align: center;
        }

        nav a {
        color: white;
        text-decoration: none;
        margin: 0 15px;
        font-weight: bold;
        }

        .hero {
        background: url('https://images.unsplash.com/photo-1599059811896-09b3b27c7b3c') no-repeat center center;
        background-size: cover;
        color: white;
        padding: 100px 20px;
        text-align: center;
        }

        .hero h1 {
        font-size: 3em;
        margin: 0;
        }

        .conteudo {
        padding: 20px;
        text-align: center;
        }

        .rodape {
        background-color: #222;
        color: white;
        text-align: center;
        padding: 15px;
        margin-top: 40px;
        }
    </style>
    </head>
    <body>

    <header>
        <h1>Academia BananaFit</h1>
        <p>Fica forte ou fica fraco, você escolhe</p>
    </header>

    <nav>
        <a href="#">Início</a>
        <a href="#">Planos</a>
        <a href="#">Contato</a>
    </nav>

    <section class="hero">
        <h1>Treine com a gente</h1>
        <p>Músculo não se constrói no sofá</p>
    </section>

    <section class="conteudo">
        <h2>Planos a partir de R$49,90</h2>
        <p>Musculação, aeróbico, funcional e mais!</p>
    </section>

    <footer class="rodape">
        <p>© 2025 BananaFit. Todos os direitos reservados.</p>
    </footer>

    </body>
    </html>
    """
    return HttpResponse(html)