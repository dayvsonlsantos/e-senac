var matriz_cores = [];
var cores = [];
var tabuleiro = [];
var movimento = 0;
var x_branco = 0;
var y_branco = 0;
var dificuldade = 100;
var jogoIniciado = false;
const MOVIMENTOS = {
    'D': 100,
    'N': 50,
    'C': 5
};

window.onload = function () {
    reset()
    nova_partida()
}

function reset() {
    movimento = 0;
    x_branco = 0;
    y_branco = 0;
    document.getElementById("resultado").innerHTML = "<strong>Dificuldade";

    const dificuldadeEscolhida = document.querySelector('input[name="dificuldade"]:checked').value;
    dificuldade = MOVIMENTOS[dificuldadeEscolhida] || MOVIMENTOS['N'];

    inicializa_variaveis();
    preenche_tabuleiro();

    document.getElementById("jogadas_realizadas").innerHTML = "Movimentos: " + movimento;
}

function novo_jogo() {
    reset();
    embaralhaTabuleiro();
    preenche_tabuleiro();
    movimento = 0;
    document.getElementById("jogadas_realizadas").innerHTML = "Movimentos: " + movimento;
    jogoIniciado = true;
}

function nova_partida() {
    movimento = 0;
    x_branco = 0;
    y_branco = 0;
    document.getElementById("resultado").innerHTML = "<strong>Dificuldade";

    const dificuldadeEscolhida = document.querySelector('input[name="dificuldade"]:checked').value;
    dificuldade = MOVIMENTOS[dificuldadeEscolhida] || MOVIMENTOS['N'];

    inicializa_variaveis();
    preenche_tabuleiro();
}

function inicializa_variaveis() {
    movimento = 0;
    document.getElementById("jogadas_realizadas").innerHTML = "Movimentos: " + movimento;
    x_branco = 0;
    y_branco = 0;

    matriz_cores = [
        ["#FF8000", "#CC0000", "#660066"],
        ["#009900", "#000000", "#FF66FF"],
        ["#66FF66", "#0000CC", "#A8A8A8"]
    ];

    cores = ["#FF8000", "#CC0000", "#660066", "#009900", "#000000", "#FF66FF", "#66FF66", "#0000CC", "#A8A8A8"];
    tabuleiro = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ];

    for (let i = 0; i < tabuleiro.length; i++) {
        for (let j = 0; j < tabuleiro[i].length; j++) {
            if (tabuleiro[i][j] === 0) {
                x_branco = i;
                y_branco = j;
                break;
            }
        }
    }
}

function preenche_tabuleiro() {
    for (let i = 0, cont = 0; i < tabuleiro.length; i++) {
        for (let j = 0; j < tabuleiro[i].length; j++, cont++) {
            const celulaTabela = document.getElementById('celula_' + (cont + 1));

            if (tabuleiro[i][j] !== 0) {
                celulaTabela.innerHTML = tabuleiro[i][j];
            } else {
                celulaTabela.innerHTML = '';
            }

            matriz_cores[i][j] = tabuleiro[i][j] !== 0 ? cores[tabuleiro[i][j] - 1] : cores[cores.length - 1];
            celulaTabela.style.background = matriz_cores[i][j];
        }
    }
}

function verifica_se_ganhou() {
    let cont = 0;
    let solucao = 1;
    for (let i = 0; i < tabuleiro.length; i++) {
        for (let j = 0; j < tabuleiro[i].length; j++) {
            cont++;
            if (tabuleiro[i][j] !== cont && cont !== 9) {
                solucao = 0;
                break;
            }
        }
        if (solucao === 0) {
            break;
        }
    }
    console.log(solucao);
    imprimir_vitoria(solucao);
}

function imprimir_vitoria(solucao) {
    const resultadoElement = document.getElementById("resultado");
    resultadoElement.innerHTML = solucao === 1 ? "Você venceu!" : "Dificuldade:";
}

function checaControles(tecla) {
    if (jogoIniciado) {
        switch (tecla) {
            case 37: // seta para a esquerda
                if (podeMoverParaEsquerda()) {
                    movePecaParaEsquerda();
                }
                break;
            case 38: // seta para cima
                if (podeMoverParaCima()) {
                    movePecaParaCima();
                }
                break;
            case 39: // seta para a direita
                if (podeMoverParaDireita()) {
                    movePecaParaDireita();
                }
                break;
            case 40: // seta para baixo
                if (podeMoverParaBaixo()) {
                    movePecaParaBaixo();
                }
                break;
            default:
                break;
        }
    }
}

function podeMoverParaEsquerda() {
    return (y_branco > 0);
}

function movePecaParaEsquerda() {
    trocaPosicao(x_branco, y_branco, x_branco, y_branco - 1);
    y_branco--;
    movimento++;
    document.getElementById("jogadas_realizadas").innerHTML = "Movimentos: " + movimento;
    preenche_tabuleiro();
    verifica_se_ganhou();
}

function podeMoverParaDireita() {
    return (y_branco < 2);
}

function movePecaParaDireita() {
    trocaPosicao(x_branco, y_branco, x_branco, y_branco + 1);
    y_branco++;
    movimento++;
    document.getElementById("jogadas_realizadas").innerHTML = "Movimentos: " + movimento;
    preenche_tabuleiro();
    verifica_se_ganhou();
}

function podeMoverParaCima() {
    return (x_branco > 0);
}

function movePecaParaCima() {
    trocaPosicao(x_branco, y_branco, x_branco - 1, y_branco);
    x_branco--;
    movimento++;
    document.getElementById("jogadas_realizadas").innerHTML = "Movimentos: " + movimento;
    preenche_tabuleiro();
    verifica_se_ganhou();
}

function podeMoverParaBaixo() {
    return (x_branco < 2);
}

function movePecaParaBaixo() {
    trocaPosicao(x_branco, y_branco, x_branco + 1, y_branco);
    x_branco++;
    movimento++;
    document.getElementById("jogadas_realizadas").innerHTML = "Movimentos: " + movimento;
    preenche_tabuleiro();
    verifica_se_ganhou();
}

function trocaPosicao(x1, y1, x2, y2) {
    const temp = tabuleiro[x1][y1];
    tabuleiro[x1][y1] = tabuleiro[x2][y2];
    tabuleiro[x2][y2] = temp;
}

function embaralhaTabuleiro() {
    for (let i = 0; i < dificuldade; i++) {
        const direcao = Math.floor(Math.random() * 4); // 0 para cima, 1 para baixo, 2 para esquerda, 3 para direita
        switch (direcao) {
            case 0: // cima
                if (podeMoverParaCima()) {
                    movePecaParaCima();
                }
                break;
            case 1: // baixo
                if (podeMoverParaBaixo()) {
                    movePecaParaBaixo();
                }
                break;
            case 2: // esquerda
                if (podeMoverParaEsquerda()) {
                    movePecaParaEsquerda();
                }
                break;
            case 3: // direita
                if (podeMoverParaDireita()) {
                    movePecaParaDireita();
                }
                break;
        }
    }
    preenche_tabuleiro()
}
