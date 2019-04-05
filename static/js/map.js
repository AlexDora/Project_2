
var myMap = L.map("map", {
  center: [23.6552843,-100.7085871],
  zoom: 4.6
});

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: 'pk.eyJ1IjoiYWxleGRvcmE5MiIsImEiOiJjanR2cmN6bTIwY24xNDNyeno3cnI0NDQwIn0.2PU5DWzYfD-RmVg5WvlgTQ'
}).addTo(myMap);


d3.json("/generaldata").then(data => {

  var markers = L.markerClusterGroup();
    // Loop through data
  for (var i = 0; i < data.coordenadas.length; i++) {
    //console.log(i)
    var coordenadas = data.coordenadas[i].split(",");
    var lat = +coordenadas[0];
    var lng = +coordenadas[1];

    // Add a new marker to the cluster group and bind a pop-up
    markers.addLayer(L.circle([lat, lng],{ color: 'yellow', radius: 50000 * (data.total_sobrepeso[i] / data.total_muestra[i])})
      .bindPopup("<h6>" + data.estados[i] + "</h6> <hr> <h9>Obesity Men: " + Math.round(100 * data.porcentaje_hombres[i]) + 
                  "%</h6> <hr> <h9>Obesity Women: " + Math.round(100 * data.porcentaje_mujeres[i]) + "%</h9>"));
    }
  myMap.addLayer(markers);
  }
)