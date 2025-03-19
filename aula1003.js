/////////////////////////////////////////
//       AULA 05 - 10.03.2025         //
///////////////////////////////////////

// ATIVIDADE 01 //

let preco = 150;
let desconto = 20;
let preco_final = preco * (desconto / 100);
console.log('O preço final é', preco_final);

// ATIVIDADE 02 //

let peso = 70;
let altura = 1.75;
let imc = peso / (altura ** 2);
console.log('O Índice de Massa Corporal vale', imc);

// ATIVIDADE 03 //

let idade = 22;
let tem_exp = true;
let concurso_eleg = idade >= 18 && tem_exp;
console.log('É elegível para o concurso?');
if (concurso_eleg) {
    console.log('Sim!')
} else {
    console.log('Não!')
}

// ATIVIDADE 04 //

let nivel_acesso = parseInt(prompt('Digite seu nível de acesso'));
if (nivel_acesso === 3) {
    console.log('Acesso total!')
} else if (nivel_acesso === 2) {
    console.log('Acesso parcial!')
} else if (nivel_acesso === 1) {
    console.log ('Acesso restrito!')
} else {
    console.log('Erro. Digite um número válido!')
}

// ATIVIDADE 05 //

let c = parseFloat(prompt('Qual a temperatura no momento?'))
let f = (((c * 9) / 5) + 32)
console.log('A temperatura marca ' + c + 'ºC ou ' + f + 'ºF!')
