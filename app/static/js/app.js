const printCharts = () => {
    renderModelsChart()
}

const renderModelsChart = () => {
    
    const data = {
        labels: ['uno', 'dos', 'tres', 'cuatro'],
        datasets: [{
            data: [10, 20 , 30, 40],
            borderColor: ['red', 'green', 'blue']
        }]
    }

    new Chart('modelsChart', {type: 'doughnut', data})

}

printCharts()