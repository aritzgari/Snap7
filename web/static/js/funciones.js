function form_desde_hasta() {
    // La idea es crear un csv o almacenar los datos que se quieren enviar
    // de vuelta como una variable global dentro del programa python y usarla más adelante en el siguiente
    var desde = document.getElementById("desde").value;
    var hasta = document.getElementById("hasta").value;
    eel.desde_hastapy(desde, hasta)();
}
function chart() {
    myChart = echarts.init(document.getElementById('main'));

    eel.devolverdatospy()().then(function ([value1, value2]) {
        var option = {
            title: {
                text: 'Datos'
            },
            tooltip: {
                trigger: 'axis'
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: value1
            },
            yAxis: {
                type: 'value'
            },
            series: [
                {
                    name: 'Entero',
                    type: 'line',
                    stack: 'Total',
                    data: value2
                }
            ]
        };
        myChart.setOption(option);
    });

};
window.onload = function createPlot() {
    eel.devolverdatospy()().then(function ([value1, value2, value3]) {
        var Contador1 = {
            x: value1,
            y: value2,
            name: "Primer Contador"
        };

        var Contador2 = {
            x: value1,
            y: value3,
            name: "Segundo Contador"
        };

        var data = [Contador1, Contador2];

        var layout = {
            title: 'Datos de aplicación',
            xaxis: {
                title: 'Tiempo'
            },
            yaxis: {
                title: 'Valor'
            }
        };
        var config={
            displaylogo: false,
            responsive: true
        };
        Plotly.newPlot('plotlygraph', data, layout, config);
    });

}