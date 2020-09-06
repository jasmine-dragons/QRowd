from ol/Map import Map
from ol/View import View
from ol/layer/Tile import TileLayer
from ol/source/OSM import OSM

var map = new Map({
  view: new View({
    center: [0, 0],
    zoom: 1
  }),
  layers: [
    new TileLayer({
      source: new OSM()
    })
  ],
  target: 'map'
});
