import gmplot

gmap = gmplot.GoogleMapPlotter(35, -102, 5)
gmap.scatter(latitudes[:1000], longitudes[:1000], 'red', size = 10)
gmap.draw('data/gmplot.html')
