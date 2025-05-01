import random
def jogo_da_forca():
    temas = {
        "T.I." : [
        "python",
        "programacao",
        "computador",
        "algoritmo",
        "desenvolvimento"
        ],

        "Animais" : [
            "porco"
            "vaca"
            "cachorro"
            "gato"
            "tartaruga"
            "peixe"
            "girafa"
            "leao"
            "zebra"
            "hipopotamo"
        ],

        "Times" : [
            "flamengo"
            "palmeiras"
            "botafogo"
            "vasco"
            "fluminense"
            "corinthians"
            "internacional"
            "cruzeiro"
            "bragantino"
            "fortaleza"
            "bahia"
            "goias"
        ]
        }
    
    tema_escolhido = random.choice(list(temas.keys()))
    palavra_secreta = random.choice(temas[tema_escolhido])
    letras_corretas = set()
    letras_erradas = set()
    vidas = 6
    
    while vidas > 0:
        # Mostra a palavra com letras adivinhadas
        palavra_exibida = "".join([letra if letra in letras_corretas else "_" for letra in palavra_secreta])
        print('\nPalavra:', ' '.join(palavra_exibida))
        print('Letras erradas:', ', '.join(sorted(letras_erradas)))

        if palavra_exibida == palavra_secreta:
            print('🎉 Parabéns! Você venceu!')
            return
        
        # Pede uma letra
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_corretas:
            print("Você já tentou essa letra.")
        elif letra in palavra_secreta:
            letras_corretas.add(letra)
            print("Letra correta!")
        else:
            vidas -= 1
            print(f"Letra incorreta! Vidas restantes: {vidas}")
    
    print(f"Game over! A palavra era: {palavra_secreta}")

jogo_da_forca()