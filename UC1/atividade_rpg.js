/////////////////////////////////////////////////////////
///                 Atividade Aula 11                 ///
/////////////////////////////////////////////////////////


/* OPÇÃO 2: Jogo de RPG Simples:
  * Crie uma classe Personagem com vida, ataque, defesa e nome.
  * Desenvolva subclasses Guerreiro, Mago e Arqueiro com habilidades especiais.
  * Implemente um sistema de batalha onde dois personagens podem lutar.
 */ 

class Personagem {
    constructor(nome, tipo, vida, ataque, defesa) {
        this.nome = nome;               // Nome do personagem
        this.tipo = tipo;               // Tipo de personagem
        this.vida = vida;               // Quantidade inicial de vida do personagem
        this.ataque = ataque;           // Quociente de ataque do personagem
        this.defesa = defesa;           // Quociente de defesa do personagem
    }

// Evento: Ataque inimigo.

    sofrerDano(dano) {
        const danoTomado = Math.max(0, dano - this.defesa);
        this.vida -= danoTomado;
        console.log(`${this.nome} foi atacado! Sofreu um dano total de ${danoTomado}! HP restante: ${this.vida}.`);
    }

    estaVivo() {
        return this.vida > 0
    }
}

class Guerreiro extends Personagem {
    constructor(nome) {
        super(nome, 'Guerreiro', 120, 15, 15);
    }
}

class Arqueiro extends Personagem {
    constructor(nome) {
        super(nome, 'Arqueiro', 80, 20, 5);
    }
}

class Mago extends Personagem {
    constructor(nome) {
        super(nome, 'Mago', 70, 25, 10)
    }
}

function batalha(jogador1, jogador2) {
    console.log(`Batalha entre ${jogador1.nome} (${jogador1.tipo}) e ${jogador2.nome} (${jogador2.tipo}) irá se iniciar!`)
    while (jogador1.estaVivo() && jogador2.estaVivo()) {
        jogador2.sofrerDano(jogador1.ataque);
        if (!jogador2.estaVivo()) {
            console.log(`${jogador2.nome} foi derrotado(a). ${jogador1.nome} é o(a) vencedor(a)!`);
            break;
        }
        jogador1.sofrerDano(jogador2.ataque);
        if (!jogador1.estaVivo()) {
            console.log(`${jogador1.nome} foi derrotado(a). ${jogador2.nome} é o(a) vencedor(a)!`);
            break;
        }
    }
}

const heroi1 = new Mago('Doutor Estranho');
const heroi2 = new Arqueiro('Gavião Arqueiro');

batalha(heroi1, heroi2);

