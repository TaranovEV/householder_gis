
var map = L.map('map').setView([55.753247, 37.620914], 10);
var marker;
var data={};
var myIcon = L.icon({
    iconUrl: '/static/marker-icon-2x-orange.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [18, 30],
    iconAnchor: [12, 30],
    popupAnchor: [1, -34],
    shadowSize: [30, 30]
    });


var newViev = JSON.parse(localStorage.getItem('newCoordMap'));
L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

if (newViev) {
    var newLat = newViev['lat'];
    var newLon = newViev['long'];
    map.setView(new L.LatLng(newLat, newLon), 15);
    localStorage.removeItem('newCoordMap');
}



map.on('click', function(e) {
    if (marker) {
        map.removeLayer(marker);
    }
    marker = new L.marker(e.latlng, {icon: myIcon}).addTo(map);
    data['lat']=e.latlng['lat'];
    data['long']=e.latlng['lng'];
});


function calculate() {
    if(data['lat']){
        var type_iso = document.getElementById("move_type");
        var time_iso = document.getElementById("move_time");
        data['type_iso']=type_iso.options[type_iso.selectedIndex].value;
        data['time_iso']=time_iso.options[time_iso.selectedIndex].value;

        document.getElementById('move_type').addEventListener('change', function() {
            data['type_iso']=this.value;
          });
        document.getElementById('move_time').addEventListener('change', function() {
            data['time_iso']=this.value;
          });
        route_url='http://127.0.0.1:8000/gis/'+data['lat']+','+data['long']+','
        +data['type_iso']+','+data['time_iso'];

        center_map = {
            lat: data['lat'], 
            long: data['long']
          };
          localStorage.setItem('newCoordMap', JSON.stringify(center_map));
        window.location.replace(route_url);
      }
    
    else {
       alert('Укажите точку расчета!');
    }
};

