/* SISTEMA ESCOLAR COM POO:

  * Crie um sistema que inclua:
  * Classe Aluno (nome, matrícula, notas, curso)
  * Métodos: calcularMedia(), adicionarNota()
  * Classe Professor (nome, departamento, disciplinas)
  * Métodos: atribuirDisciplina(), listarTurmas()
  * Classe Disciplina (nome, código, alunosMatriculados)
  * Métodos: matricularAluno(), gerarBoletim()

  * Classe Escola (nome, listaAlunos, listaProfessores)
  * Métodos: matricularAluno(), contratarProfessor(), gerarRelatorio()

  * Implemente interações entre todas as classes e um menu básico no console para testar todas as funcionalidades.
*/

class Escola {
    constructor(nome) {
        this.nome = nome;
        this.listaAlunos = [];
        this.listaProfessores = [];
    }

    // Função para matricular o aluno na escola
    matricularAluno(aluno) {
        this.listaAlunos.push(aluno);
    }

    // Função para contratar professores
    contratarProfessor(professor) {
        this.listaProfessores.push(professor);
    }

    // Gerar relatório de alunos matriculados e professores contratados
    gerarRelatorio() {
        const alunosMatriculados = Object.keys(this.listaAlunos);
        if (alunosMatriculados.length > 0) {
            console.log(`Alunos matriculados em ${this.nome}: ${this.listaAlunos}`);
            alunosMatriculados.forEach(aluno => console.log(`${aluno}\n)`));
        } else {
            console.log(`Nenhum aluno matriculado em ${this.nome}.`);
        }

        const professoresContratados = Object.keys(this.listaProfessores);
        if (professoresContratados.length > 0) {
            console.log(`Professores contratados: ${this.listaProfessores}`);
            professoresContratados.forEach(professor => console.log(`${professor}\n`));
        } else {
            console.log(`Nenhum professor contratado`);
        }
    }
}

// Teste

const escola = new Escola('Rakel Rechuem');

matricularAluno('Pedro Costa Cordeiro');
matricularAluno('Rafael de Oliveira Meira');
matricularAluno('Victor Hugo Dias de Oliveira');
matricularAluno('Carlos Gabriel de Barros Felipe');
contratarProfessor('André Lessa Felipe');
contratarProfessor('Carlos Rivero');
contratarProfessor('Vinícius Zanardi');
gerarRelatorio();