// ATIVIDADE 01
// Cálculo de Média de Notas: Peça ao usuário que insira 4 notas (de 0 a 10).
// Calcule a média das notas e exiba o resultado.
// Se a média for maior ou igual a 7, exiba "Aprovado". Caso contrário, exiba "Reprovado".

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function notas(p1, p2, p3, p4) {
    medianotas = (p1 + p2 + p3 + p4) / 4
    if (medianotas >= 7) {
        return 'Você está aprovado!'
    } else {
        return 'Você está reprovado!'
    }
}

rl.question('Nota 1: ', (p1) => {
    rl.question('Nota 2: ', (p2) => {
        rl.question('Nota 3: ', (p3) => {
            rl.question('Nota 4: ', (p4) => {

                p1 = parseFloat(p1);
                p2 = parseFloat(p2);
                p3 = parseFloat(p3);
                p4 = parseFloat(p4);

                let resultado = notas(p1, p2, p3, p4);
                console.log(`Sua média: ${medianotas}\n${resultado}\n`);

                rl.close();
            });
        });
    });
});

// ATIVIDADE 02
// Soma dos Números Pares em um Intervalo:
// Peça ao usuário dois números, representando o início e o fim de um intervalo.
// Use um loop (for ou while) para calcular a soma de todos os números pares nesse intervalo e exiba o resultado.

