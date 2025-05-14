from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Academia X - Início</title>
        <style>
            body { font-family: Arial; margin: 0; padding: 0; background: #e0f7fa; color: #333; }
            header, footer { background: #00796b; color: white; padding: 20px; text-align: center; }
            nav { background: #004d40; padding: 10px; text-align: center; }
            nav a { color: white; margin: 0 15px; text-decoration: none; font-weight: bold; }
            section { padding: 30px; text-align: center; }
        </style>
    </head>
    <body>
        <header><h1>Academia X</h1></header>
        <nav>
            <a href="/">Início</a>
            <a href="/planos/">Planos</a>
            <a href="/contato/">Contato</a>
        </nav>
        <section>
            <h2>Bem-vindo à nossa academia!</h2>
            <p>Fica forte ou fica fraco, você escolhe 💪</p>
        </section>
        <footer>© 2025 Academia X - Todos os direitos reservados.</footer>
    </body>
    </html>
    """
    return HttpResponse(html)

def planos(request):
    html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Academia X - Planos</title>
        <style>
            body { font-family: Arial; margin: 0; padding: 0; background: #fff3e0; color: #333; }
            header, footer { background: #f57c00; color: white; padding: 20px; text-align: center; }
            nav { background: #ef6c00; padding: 10px; text-align: center; }
            nav a { color: white; margin: 0 15px; text-decoration: none; font-weight: bold; }
            section { padding: 30px; text-align: center; }
        </style>
    </head>
    <body>
        <header><h1>Nossos Planos 🏋️</h1></header>
        <nav>
            <a href="/">Início</a>
            <a href="/planos/">Planos</a>
            <a href="/contato/">Contato</a>
        </nav>
        <section>
            <h2>Planos a partir de R$49,90</h2>
            <p>Inclui musculação, funcional, aeróbico e muito mais!</p>
        </section>
        <footer>© 2025 Academia X - Todos os direitos reservados.</footer>
    </body>
    </html>
    """
    return HttpResponse(html)

def contato(request):
    html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Academia X - Contato</title>
        <style>
            body { font-family: Arial; margin: 0; padding: 0; background: #ede7f6; color: #333; }
            header, footer { background: #512da8; color: white; padding: 20px; text-align: center; }
            nav { background: #673ab7; padding: 10px; text-align: center; }
            nav a { color: white; margin: 0 15px; text-decoration: none; font-weight: bold; }
            section { padding: 30px; text-align: center; }
        </style>
    </head>
    <body>
        <header><h1>Fale com a gente 📞</h1></header>
        <nav>
            <a href="/">Início</a>
            <a href="/planos/">Planos</a>
            <a href="/contato/">Contato</a>
        </nav>
        <section>
            <h2>Endereço:</h2>
            <p>Rua do Bíceps, nº 71, Mesquita - RJ</p>
            <h2>WhatsApp:</h2>
            <p>(21) 99999-0000</p>
        </section>
        <footer>© 2025 Academia X - Todos os direitos reservados.</footer>
    </body>
    </html>
    """
    return HttpResponse(html)