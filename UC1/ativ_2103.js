
// 1. Soma de Matrizes: Crie duas matrizes 3x3 e escreva uma função para somá-las. A função deve retornar uma nova matriz com o resultado.

function somarMatrizes(mtr1, mtr2) {
    let resultado = [];
    for (let i = 0; i < 3; i++) {
        resultado[i] = [];
        for (let j = 0; j < 3; j++) {
            resultado[i][j] = mtr1[i][j] + mtr2[i][j];
        }
    }
    return resultado;
}

let mtr1 = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
];

let mtr2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

let resultado = somarMatrizes(mtr1, mtr2);

console.log('Resultado da soma das matrizes:', resultado);


// 2. Transposição de Matriz: Escreva uma função que receba uma matriz 3x3 e retorne sua transposta (troque linhas por colunas).

// Minha tentativa
function transporMatriz() {
    for (let i = 0; i < matriz.length; i++) {
        for (let j = 0; j < matriz[i].length; j++){
            let matriztransposta = matriz
            console.log('A matriz transposta é:')
        }
    }
}

let matriz = [
    
]

// ChatGPT
function transporMatriz(matriz) {
    let transposta = [];
    for (let i = 0; i < matriz.length; i++) {
        transposta[i] = []
        for (let j = 0; j < matriz[i].length; j++) {
            transposta[i][j] = matriz[j][i];
        }
    }
    return transposta;
}

let matrizOriginal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

console.log(transporMatriz(matrizOriginal));


// 3. Multiplicação de Matrizes: Crie duas matrizes 2x2 e escreva uma função para multiplicá-las.

function multiplicarMatrizes(matriz1, matriz2) {
    let resultado = [];
    for (let i = 0; i < 2; i++) {
        resultado[i] = [];
        for (let j = 0; j < 2; j++) {
            resultado[i][j] = matriz1[i][j] * matriz2[i][j]
        }
    }
    return resultado;
}

let matriz1 = [
    [2, 3],
    [5, 4]
];

let matriz2 = [
    [7, 6],
    [3, 5]
];

let multiplicacao = multiplicarMatrizes(matriz1, matriz2);

console.log('O resultado da multiplicação é:', multiplicacao);


// 4. Jogo da Velha: Implemente um jogo da velha usando uma matriz 3x3. O programa deve permitir que dois jogadores façam jogadas alternadas e verifique se há um vencedor.

// Jogo da Velha - Tabuleiro inicial
let jogodavelha = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
];

// Função para a jogabilidade do jogador X
function colocarX(linha, coluna) {
    if (jogodavelha[linha][coluna] === '') {
        jogodavelha[linha][coluna] = 'X'
        console.log(jogodavelha);
    } else {
        console.log('Espaço já preenchido')
    }
        if (jogodavelha[0][0] && jogodavelha[1][1] && jogodavelha[2][2] || 
        jogodavelha[0][2] && jogodavelha[1][1] && jogodavelha[2][0] || 
        jogodavelha[0][0] && jogodavelha[0][1] && jogodavelha[0][2] || 
        jogodavelha[1][0] && jogodavelha[1][1] && jogodavelha[1][2] ||
        jogodavelha[2][0] && jogodavelha[2][1] && jogodavelha[2][2] === 'X') {
            console.log('X é o vencedor!')
        }
}

// Função para a jogabilidade do jogador Y
function colocarY(linha, coluna) {
    if (jogodavelha[linha][coluna] === '') {
    jogodavelha[linha][coluna] = 'Y'
        console.log(jogodavelha);
    } else {
        console.log('Espaço já preenchido');
    }
        if (jogodavelha[0][0] && jogodavelha[1][1] && jogodavelha[2][2] || 
        jogodavelha[0][2] && jogodavelha[1][1] && jogodavelha[2][0] || 
        jogodavelha[0][0] && jogodavelha[0][1] && jogodavelha[0][2] || 
        jogodavelha[1][0] && jogodavelha[1][1] && jogodavelha[1][2] ||
        jogodavelha[2][0] && jogodavelha[2][1] && jogodavelha[2][2] === 'O') {
            console.log('O é o vencedor!')
        }
}

// Testando a função:
colocarX(0, 2);


// 5. Busca em Matriz: Escreva uma função que receba uma matriz e um número, e retorne a posição (linha e coluna) desse número na matriz.
// Se o número não estiver na matriz, retorne null.

function identificarNumero(mtriz, numero) {
    for (let i = 0; i < mtriz.length; i++) {
        for (let j = 0; j < mtriz[i].length; j++) {
            if (mtriz[i][j] === numero) {
                return {linha: i, coluna: j};
            }
        }
    }
    return null;
}

let mtriz = [
    [5, 9, 3],
    [6, 7, 1],
    [2, 8, 0]
];

console.log(identificarNumero(mtriz, 5));


// 6. Matriz Identidade: Crie uma função que gere uma matriz identidade de tamanho NxN (uma matriz onde os elementos da diagonal principal são 1 e os demais são 0).

function matrizIdentidade(N) {
    let matriz2 = [];

    for (let i = 0; i < N; i++) {
        let linha = [];
        for (let j = 0; j < N; j++) {
            if (i === j) {
                linha.push(1);
            } else {
                linha.push(0);
            }
        }
        matriz2.push(linha);
    }

    return matriz2;
}

console.log(matrizIdentidade(3));


// 7. Rotação de Matriz: Escreva uma função que rotacione uma matriz 3x3 em 90 graus no sentido horário.

function rotacaoDeMatriz(linha, coluna) {
    
}


// 8. Soma das Bordas: Escreva uma função que calcule a soma dos elementos das bordas de uma matriz NxN.