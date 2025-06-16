const nodesChartCtx = document.getElementById('nodesChart').getContext('2d');
const timeChartCtx = document.getElementById('timeChart').getContext('2d');

const nodesChart = new Chart(nodesChartCtx, {
    type: 'bar',
    data: {
        labels: ['Backtracking', 'Branch & Bound'],
        datasets: [{
            label: 'Nodos Explorados',
            data: [
                solutionData.backtracking.nodes_explored,
                solutionData.branchbound.nodes_explored
            ],
            backgroundColor: ['#4CAF50', '#2196F3']
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: false },
            title: {
                display: true,
                text: 'Nodos Explorados por Algoritmo'
            }
        },
        scales: {
            y: { beginAtZero: true }
        }
    }
});

const timeChart = new Chart(timeChartCtx, {
    type: 'bar',
    data: {
        labels: ['Backtracking', 'Branch & Bound'],
        datasets: [{
            label: 'Tiempo de Ejecución (s)',
            data: [
                solutionData.backtracking.time.toFixed(4),
                solutionData.branchbound.time.toFixed(4)
            ],
            backgroundColor: ['#4CAF50', '#2196F3']
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: false },
            title: {
                display: true,
                text: 'Tiempo de Ejecución por Algoritmo (segundos)'
            }
        },
        scales: {
            y: { beginAtZero: true }
        }
    }
});
