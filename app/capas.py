import geopandas as gpd 
#import Folium 
#import webbrowser


ruta_shape = "/shape_files/ign_departamento.shp"
dptos = gpd.read_file(ruta_shape)

print("Tipo de datos:")
print(type(dptos))

print("\nColumnas del archivo shape: ")
print(dptos.columns)

print("\nGeoseries: ")
print(type(dptos.geometry))

#mapa

#mimapa = folium.Map(
#    location=[-33.337528338594026, -66.30829314167931], 
#    zoom_start = 8,
#    tiles='cartodb positron' #OpenStreetMap
#)

