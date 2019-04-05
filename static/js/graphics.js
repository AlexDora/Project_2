
d3.json("/generaldata").then(data => {

  var x_values = data.estados;
  var m_values = data.porcentaje_mujeres;
  var h_values = data.porcentaje_hombres;

  var trace1 = {
    x: x_values,
    y: m_values,
    type: 'bar',
    name: 'Women'
  };

  var trace2 = {
    x: x_values,
    y: h_values,
    type: 'bar',
    name: 'Men'
  };

  var data = [trace1, trace2];
  var layout = {barmode: 'group'};

  Plotly.newPlot('myDiv', data, layout);
});
