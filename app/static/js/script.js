document.addEventListener('DOMContentLoaded', () => {
    const tabela = document.querySelector('#table-rank tbody');

    const linhas = Array.from(tabela.querySelectorAll('tr'));

    linhas.forEach(linha => {
        const vitoria = parseInt(linha.cells[4].textContent) || 0;
        const empates = parseInt(linha.cells[5].textContent) || 0;
        const derrota = parseInt(linha.cells[6].textContent) || 0;
        const golsPro = parseInt(linha.cells[7].textContent) || 0;
        const golsContra = parseInt(linha.cells[8].textContent) || 0;

        const pontos = (vitoria * 3) + empates
        const jogos = vitoria + empates + derrota
        const saldoGols = golsPro - golsContra;
        const aprov = ((pontos / jogos) * 0.33333) * 100

        linha.cells[2].textContent = pontos;
        linha.cells[3].textContent = jogos
        linha.cells[9].textContent = saldoGols;
        linha.cells[10].textContent = aprov.toFixed(2) + " % ";

    });

    linhas.sort((a, b) => {

        const pontoA = parseInt(a.cells[2].textContent);
        const pontoB = parseInt(b.cells[2].textContent);
        const vitoriaA = parseInt(a.cells[4].textContent);
        const vitoriaB = parseInt(b.cells[4].textContent);
        const saldoA = parseInt(a.cells[9].textContent);
        const saldoB = parseInt(b.cells[9].textContent);
        const golsProA = parseInt(a.cells[7].textContent);
        const golsProB = parseInt(b.cells[7].textContent);


        if (pontoB !== pontoA) return pontoB - pontoA;

        if (vitoriaB !== vitoriaA) return vitoriaB - vitoriaA;

        if (saldoB !== saldoA) return saldoB - saldoA;

        if (golsProB !== golsProA) return golsProB - golsProA;
        return 0;
    });

    linhas.forEach((linha, index) => {
        linha.cells[0].textContent = index + 1;
        tabela.appendChild(linha);
    });
});

function trocarID(id) {
    const divs = document.querySelectorAll('#pontosjogador, #artilharia, #gamerjogador');

    divs.forEach(div => {
        div.style.display = 'none';
    });
    document.getElementById(id).style.display = 'block';
}

function mostrarEsconder(id) {

    const divs = document.querySelectorAll('#noticias, #sobre');

    divs.forEach(div => {
        div.style.display = 'none';
    });
    document.getElementById(id).style.display = 'block';
}

function mostrarEsconderII(id) {

    const divs = document.querySelectorAll('#classificao-geral, #table-grupos, #table-mata');

    divs.forEach(div => {
        div.style.display = 'none';
    });
    document.getElementById(id).style.display = 'block';
}

document.addEventListener('DOMContentLoaded', () => {
    const tabela = document.querySelector('#table-grupoA tbody, #table-grupoB tbody');

    const linhas = Array.from(tabela.querySelectorAll('tr'));

    linhas.forEach(linha => {
        const vitoria = parseInt(linha.cells[4].textContent) || 0;
        const empates = parseInt(linha.cells[5].textContent) || 0;
        const derrota = parseInt(linha.cells[6].textContent) || 0;
        const golsPro = parseInt(linha.cells[7].textContent) || 0;
        const golsContra = parseInt(linha.cells[8].textContent) || 0;

        const pontos = (vitoria * 3) + empates
        const jogos = vitoria + empates + derrota
        const saldoGols = golsPro - golsContra;
        const aprov = ((pontos / jogos) * 0.33333) * 100

        linha.cells[2].textContent = pontos;
        linha.cells[3].textContent = jogos
        linha.cells[9].textContent = saldoGols;
        linha.cells[10].textContent = aprov.toFixed(2) + " % ";

    });

    linhas.sort((a, b) => {

        const pontoA = parseInt(a.cells[2].textContent);
        const pontoB = parseInt(b.cells[2].textContent);
        const vitoriaA = parseInt(a.cells[4].textContent);
        const vitoriaB = parseInt(b.cells[4].textContent);
        const saldoA = parseInt(a.cells[9].textContent);
        const saldoB = parseInt(b.cells[9].textContent);
        const golsProA = parseInt(a.cells[7].textContent);
        const golsProB = parseInt(b.cells[7].textContent);


        if (pontoB !== pontoA) return pontoB - pontoA;

        if (vitoriaB !== vitoriaA) return vitoriaB - vitoriaA;

        if (saldoB !== saldoA) return saldoB - saldoA;

        if (golsProB !== golsProA) return golsProB - golsProA;
        return 0;
    });

    linhas.forEach((linha, index) => {
        linha.cells[0].textContent = index + 1;

        linha.classList.remove('g2', 'z2');

        if (index <= 1) {
            linha.classList.add('g2');
        } else if (index >= 2) {
            linha.classList.add('z2')
        }
        tabela.appendChild(linha);
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const tabela = document.querySelector('#table-grupoB tbody');

    const linhas = Array.from(tabela.querySelectorAll('tr'));

    linhas.forEach(linha => {
        const vitoria = parseInt(linha.cells[4].textContent) || 0;
        const empates = parseInt(linha.cells[5].textContent) || 0;
        const derrota = parseInt(linha.cells[6].textContent) || 0;
        const golsPro = parseInt(linha.cells[7].textContent) || 0;
        const golsContra = parseInt(linha.cells[8].textContent) || 0;

        const pontos = (vitoria * 3) + empates
        const jogos = vitoria + empates + derrota
        const saldoGols = golsPro - golsContra;
        const aprov = ((pontos / jogos) * 0.33333) * 100

        linha.cells[2].textContent = pontos;
        linha.cells[3].textContent = jogos
        linha.cells[9].textContent = saldoGols;
        linha.cells[10].textContent = aprov.toFixed(2) + " % ";

    });

    linhas.sort((a, b) => {

        const pontoA = parseInt(a.cells[2].textContent);
        const pontoB = parseInt(b.cells[2].textContent);
        const vitoriaA = parseInt(a.cells[4].textContent);
        const vitoriaB = parseInt(b.cells[4].textContent);
        const saldoA = parseInt(a.cells[9].textContent);
        const saldoB = parseInt(b.cells[9].textContent);
        const golsProA = parseInt(a.cells[7].textContent);
        const golsProB = parseInt(b.cells[7].textContent);


        if (pontoB !== pontoA) return pontoB - pontoA;

        if (vitoriaB !== vitoriaA) return vitoriaB - vitoriaA;

        if (saldoB !== saldoA) return saldoB - saldoA;

        if (golsProB !== golsProA) return golsProB - golsProA;
        return 0;
    });

    linhas.forEach((linha, index) => {
        linha.cells[0].textContent = index + 1;

        linha.classList.remove('g2', 'z2');

        if (index <= 1) {
            linha.classList.add('g2');
        } else if (index >= 2) {
            linha.classList.add('z2')
        }
        tabela.appendChild(linha);
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const tabela = document.querySelector('#table-grupoC tbody');

    const linhas = Array.from(tabela.querySelectorAll('tr'));

    linhas.forEach(linha => {
        const vitoria = parseInt(linha.cells[4].textContent) || 0;
        const empates = parseInt(linha.cells[5].textContent) || 0;
        const derrota = parseInt(linha.cells[6].textContent) || 0;
        const golsPro = parseInt(linha.cells[7].textContent) || 0;
        const golsContra = parseInt(linha.cells[8].textContent) || 0;

        const pontos = (vitoria * 3) + empates
        const jogos = vitoria + empates + derrota
        const saldoGols = golsPro - golsContra;
        const aprov = ((pontos / jogos) * 0.33333) * 100

        linha.cells[2].textContent = pontos;
        linha.cells[3].textContent = jogos
        linha.cells[9].textContent = saldoGols;
        linha.cells[10].textContent = aprov.toFixed(2) + " % ";

    });

    linhas.sort((a, b) => {

        const pontoA = parseInt(a.cells[2].textContent);
        const pontoB = parseInt(b.cells[2].textContent);
        const vitoriaA = parseInt(a.cells[4].textContent);
        const vitoriaB = parseInt(b.cells[4].textContent);
        const saldoA = parseInt(a.cells[9].textContent);
        const saldoB = parseInt(b.cells[9].textContent);
        const golsProA = parseInt(a.cells[7].textContent);
        const golsProB = parseInt(b.cells[7].textContent);


        if (pontoB !== pontoA) return pontoB - pontoA;

        if (vitoriaB !== vitoriaA) return vitoriaB - vitoriaA;

        if (saldoB !== saldoA) return saldoB - saldoA;

        if (golsProB !== golsProA) return golsProB - golsProA;
        return 0;
    });

    linhas.forEach((linha, index) => {
        linha.cells[0].textContent = index + 1;

        linha.classList.remove('g2', 'z2');

        if (index <= 1) {
            linha.classList.add('g2');
        } else if (index >= 2) {
            linha.classList.add('z2')
        }
        tabela.appendChild(linha);
    });
});

//Grupo D
document.addEventListener('DOMContentLoaded', () => {
    const tabela = document.querySelector('#table-grupoD tbody');

    const linhas = Array.from(tabela.querySelectorAll('tr'));

    linhas.forEach(linha => {
        const vitoria = parseInt(linha.cells[4].textContent) || 0;
        const empates = parseInt(linha.cells[5].textContent) || 0;
        const derrota = parseInt(linha.cells[6].textContent) || 0;
        const golsPro = parseInt(linha.cells[7].textContent) || 0;
        const golsContra = parseInt(linha.cells[8].textContent) || 0;

        const pontos = (vitoria * 3) + empates
        const jogos = vitoria + empates + derrota
        const saldoGols = golsPro - golsContra;
        const aprov = ((pontos / jogos) * 0.33333) * 100

        linha.cells[2].textContent = pontos;
        linha.cells[3].textContent = jogos
        linha.cells[9].textContent = saldoGols;
        linha.cells[10].textContent = aprov.toFixed(2) + " % ";

    });

    linhas.sort((a, b) => {

        const pontoA = parseInt(a.cells[2].textContent);
        const pontoB = parseInt(b.cells[2].textContent);
        const vitoriaA = parseInt(a.cells[4].textContent);
        const vitoriaB = parseInt(b.cells[4].textContent);
        const saldoA = parseInt(a.cells[9].textContent);
        const saldoB = parseInt(b.cells[9].textContent);
        const golsProA = parseInt(a.cells[7].textContent);
        const golsProB = parseInt(b.cells[7].textContent);


        if (pontoB !== pontoA) return pontoB - pontoA;

        if (vitoriaB !== vitoriaA) return vitoriaB - vitoriaA;

        if (saldoB !== saldoA) return saldoB - saldoA;

        if (golsProB !== golsProA) return golsProB - golsProA;
        return 0;
    });

    linhas.forEach((linha, index) => {
        linha.cells[0].textContent = index + 1;

        linha.classList.remove('g2', 'z2');

        if (index <= 1) {
            linha.classList.add('g2');
        } else if (index >= 2) {
            linha.classList.add('z2')
        }


        tabela.appendChild(linha);
    });
});

function mudarFinal(id) {

    const divs = document.querySelectorAll('#quartasFinais, #semiFinais, #finais');

    divs.forEach(div => {
        div.style.display = 'none';
    });
    document.getElementById(id).style.display = 'block';
}
