// Labirinto inicial (matriz 5x5). 
// O labirinto é representado como uma matriz de 5x5 onde cada número indica se a célula é um caminho livre (0) ou uma parede (1).
let maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0]
];

// Coordenadas do ponto de início e do objetivo no labirinto.
// O ponto de início está na célula (0, 0) e o objetivo está na célula (4, 4).
let start = [0, 0];
let goal = [4, 4];

// Função para desenhar o labirinto e o caminho encontrado
function drawMaze(path = []) {
    // Obtém o elemento HTML onde o labirinto será desenhado
    const mazeElement = document.getElementById('maze');
    mazeElement.innerHTML = ''; // Limpa o conteúdo existente no elemento

    // Percorre todas as células da matriz do labirinto
    for (let r = 0; r < 5; r++) {
        for (let c = 0; c < 5; c++) {
            const cell = document.createElement('div'); // Cria um novo elemento div para cada célula
            cell.className = 'cell'; // Adiciona a classe 'cell' para estilização

            // Verifica se a célula é uma parede
            if (maze[r][c] === 1) {
                cell.classList.add('wall'); // Adiciona a classe 'wall' para células de parede
            }
            // Verifica se a célula é o ponto de início
            if (r === start[0] && c === start[1]) {
                cell.classList.add('start'); // Adiciona a classe 'start' para o ponto de início
            }
            // Verifica se a célula é o objetivo
            if (r === goal[0] && c === goal[1]) {
                cell.classList.add('end'); // Adiciona a classe 'end' para o ponto de objetivo
            }
            // Verifica se a célula faz parte do caminho encontrado
            if (path.some(p => p[0] === r && p[1] === c)) {
                cell.classList.add('path'); // Adiciona a classe 'path' para o caminho encontrado
            }
            mazeElement.appendChild(cell); // Adiciona a célula ao elemento HTML do labirinto
        }
    }
}

// Implementa a busca em largura (BFS)
function bfs() {
    // Direções possíveis para se mover (direita, baixo, esquerda, cima)
    const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];

    // Fila para armazenar os caminhos a serem explorados, começando pelo ponto de início
    const queue = [[start]];

    // Conjunto para rastrear células já visitadas
    const visited = new Set();
    visited.add(start.toString()); // Marca o ponto de início como visitado

    // Enquanto houver caminhos a explorar na fila
    while (queue.length > 0) {
        const path = queue.shift(); // Remove o caminho mais antigo da fila
        const [r, c] = path[path.length - 1]; // Obtém a última célula do caminho atual

        // Verifica se o objetivo foi alcançado
        if (r === goal[0] && c === goal[1]) {
            return path; // Retorna o caminho encontrado até o objetivo
        }

        // Explora as células adjacentes
        for (const [dr, dc] of directions) {
            const nr = r + dr; // Nova linha
            const nc = c + dc; // Nova coluna

            // Verifica se a nova célula está dentro dos limites do labirinto e é um caminho livre
            if (nr >= 0 && nr < 5 && nc >= 0 && nc < 5 && maze[nr][nc] === 0) {
                const next = [nr, nc]; // Nova célula a ser explorada
                if (!visited.has(next.toString())) {
                    visited.add(next.toString()); // Marca a nova célula como visitada
                    queue.push([...path, next]); // Adiciona o novo caminho à fila
                }
            }
        }
    }
    return []; // Retorna um array vazio se não encontrar um caminho
}

// Implementa a busca em profundidade (DFS)
function dfs() {
    // Direções possíveis para se mover (direita, baixo, esquerda, cima)
    const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];

    // Pilha para armazenar os caminhos a serem explorados, começando pelo ponto de início
    const stack = [[start]];

    // Conjunto para rastrear células já visitadas
    const visited = new Set();
    visited.add(start.toString()); // Marca o ponto de início como visitado

    // Enquanto houver caminhos a explorar na pilha
    while (stack.length > 0) {
        const path = stack.pop(); // Remove o caminho mais recente da pilha
        const [r, c] = path[path.length - 1]; // Obtém a última célula do caminho atual

        // Verifica se o objetivo foi alcançado
        if (r === goal[0] && c === goal[1]) {
            return path; // Retorna o caminho encontrado até o objetivo
        }

        // Explora as células adjacentes
        for (const [dr, dc] of directions) {
            const nr = r + dr; // Nova linha
            const nc = c + dc; // Nova coluna

            // Verifica se a nova célula está dentro dos limites do labirinto e é um caminho livre
            if (nr >= 0 && nr < 5 && nc >= 0 && nc < 5 && maze[nr][nc] === 0) {
                const next = [nr, nc]; // Nova célula a ser explorada
                if (!visited.has(next.toString())) {
                    visited.add(next.toString()); // Marca a nova célula como visitada
                    stack.push([...path, next]); // Adiciona o novo caminho à pilha
                }
            }
        }
    }
    return []; // Retorna um array vazio se não encontrar um caminho
}

// Função heurística para calcular a distância de Manhattan entre duas células
// A distância de Manhattan é a soma das diferenças absolutas das coordenadas
function heuristic(a, b) {
    return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
}

// Implementa a busca gulosa (Greedy Best-First Search)
function greedy() {
    // Direções possíveis para se mover (direita, baixo, esquerda, cima)
    const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];

    // Lista de caminhos a serem explorados, começando pelo ponto de início
    // Cada item da lista é um caminho, com o último elemento do caminho sendo a célula atual
    const openList = [[start]];

    // Conjunto para rastrear células já visitadas
    const visited = new Set();
    visited.add(start.toString()); // Marca o ponto de início como visitado

    // Enquanto houver caminhos a explorar na lista aberta
    while (openList.length > 0) {
        // Ordena a lista aberta pela distância heurística para o objetivo
        openList.sort((a, b) => heuristic(a[a.length - 1], goal) - heuristic(b[b.length - 1], goal));
        const path = openList.shift(); // Remove o caminho com a menor distância heurística
        const [r, c] = path[path.length - 1]; // Obtém a última célula do caminho atual

        // Verifica se o objetivo foi alcançado
        if (r === goal[0] && c === goal[1]) {
            return path; // Retorna o caminho encontrado até o objetivo
        }

        // Explora as células adjacentes
        for (const [dr, dc] of directions) {
            const nr = r + dr; // Nova linha
            const nc = c + dc; // Nova coluna

            // Verifica se a nova célula está dentro dos limites do labirinto e é um caminho livre
            if (nr >= 0 && nr < 5 && nc >= 0 && nc < 5 && maze[nr][nc] === 0) {
                const next = [nr, nc]; // Nova célula a ser explorada
                if (!visited.has(next.toString())) {
                    visited.add(next.toString()); // Marca a nova célula como visitada
                    openList.push([...path, next]); // Adiciona o novo caminho à lista aberta
                }
            }
        }
    }
    return []; // Retorna um array vazio se não encontrar um caminho
}

// Implementa a busca A* (A Star)
function aStar() {
    // Direções possíveis para se mover (direita, baixo, esquerda, cima)
    const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];

    // Lista de caminhos a serem explorados, começando pelo ponto de início
    // Cada item na lista é um array com dois elementos:
    // 1. O custo total estimado (f) do caminho até agora
    // 2. O próprio caminho até a célula atual
    const openList = [[0, [start]]]; // A primeira célula na lista aberta tem custo total (f) de 0

    // Conjunto para rastrear células já visitadas
    const visited = new Set();

    // Mapa para armazenar o custo acumulado para chegar a cada célula
    const gScore = new Map();
    gScore.set(start.toString(), 0); // O custo inicial para o ponto de início é 0

    // Enquanto houver caminhos a explorar na lista aberta
    while (openList.length > 0) {
        // Ordena a lista aberta pelo custo total (f) mais baixo
        openList.sort((a, b) => a[0] - b[0]);
        const [f, path] = openList.shift(); // Remove o caminho com o menor custo total
        const [r, c] = path[path.length - 1]; // Obtém a última célula do caminho atual

        // Verifica se o objetivo foi alcançado
        if (r === goal[0] && c === goal[1]) {
            return path; // Retorna o caminho encontrado até o objetivo
        }

        // Explora as células adjacentes
        for (const [dr, dc] of directions) {
            const nr = r + dr; // Nova linha
            const nc = c + dc; // Nova coluna

            // Verifica se a nova célula está dentro dos limites do labirinto e é um caminho livre
            if (nr >= 0 && nr < 5 && nc >= 0 && nc < 5 && maze[nr][nc] === 0) {
                const next = [nr, nc]; // Nova célula a ser explorada
                // Calcula o custo acumulado para chegar à nova célula
                const nextG = (gScore.get(path[path.length - 1].toString()) || 0) + 1;
                // Calcula o custo total (f) como a soma do custo acumulado (g) e a heurística para o objetivo
                const nextF = nextG + heuristic(next, goal);

                // Adiciona o novo caminho à lista aberta se não foi visitado ou se o novo custo é menor
                if (!visited.has(next.toString()) || nextG < gScore.get(next.toString())) {
                    visited.add(next.toString()); // Marca a nova célula como visitada
                    gScore.set(next.toString(), nextG); // Atualiza o custo acumulado para a nova célula
                    openList.push([nextF, [...path, next]]); // Adiciona o novo caminho à lista aberta com custo total
                }
            }
        }
    }
    return []; // Retorna um array vazio se não encontrar um caminho
}

// Função para executar o algoritmo escolhido
// A função recebe o nome do algoritmo a ser utilizado e executa a busca correspondente
function runAlgorithm(algorithm) {
    let path;
    // Verifica qual algoritmo foi solicitado
    switch (algorithm) {
        case 'bfs':
            path = bfs(); // Executa a busca em largura
            break;
        case 'dfs':
            path = dfs(); // Executa a busca em profundidade
            break;
        case 'greedy':
            path = greedy(); // Executa a busca gulosa
            break;
        case 'aStar':
            path = aStar(); // Executa a busca A*
            break;
    }
    drawMaze(path); // Desenha o labirinto com o caminho encontrado pelo algoritmo
}

// Atualiza o labirinto com novos pontos de início e objetivo
// Lê as novas posições a partir dos campos de entrada e redesenha o labirinto
function updateMaze() {
    // Obtém as coordenadas do ponto de início e objetivo a partir dos campos de entrada
    const startInput = document.getElementById('start').value.split(',').map(Number);
    const goalInput = document.getElementById('goal').value.split(',').map(Number);

    // Verifica se as entradas têm exatamente dois valores (linha e coluna)
    if (startInput.length === 2 && goalInput.length === 2) {
        start = startInput; // Atualiza o ponto de início
        goal = goalInput; // Atualiza o ponto de objetivo
        drawMaze(); // Redesenha o labirinto com as novas posições
    }
}

// Inicializa o labirinto na primeira carga da página
// Desenha o labirinto com o ponto de início e objetivo padrão
drawMaze();

