const ctxDoughnut = document.getElementById('myDoughnutChart');
    
        new Chart(ctxDoughnut, {
            type: 'doughnut',
            data: {
                labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple'],
                datasets: [{
                    data: [7, 12, 3, 9, 5],
                    backgroundColor: ['red', 'blue', 'yellow', 'green', 'purple']
                }]
            }
        });