from fastapi import FastAPI, Response, Request # type: ignore

import folium # type: ignore
import geopandas as gpd 

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a la aplicación del Cuaderno de Campo Digital!"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    # Lógica para obtener el item_id de la base de datos
    return {"item": f"Elemento con ID {item_id}"}

@app.get("/mapa")
def get_mapa():
    # Lógica para generar el mapa
    # mapa = folium.Map(location=[-33.337528338594026, -66.30829314167931], zoom_start=8, tiles='cartodb positron')

    ruta_shape = "/shape_files/ign_departamento.shp"
    #dptos = gpd.read_file(ruta_shape)

    # tipos = dptos
    # columnas = dptos.columns
    # geom = dptos.geometry

    #map_html = mapa._repr_html_(tipos, columnas, geom)

    #tipos = "tipos de datos: " + str(type(dptos)) + "\n columnas: " + str(dptos.columns) + "\n geoseries: " + str(type(dptos.geometry))
    
    # Return the HTML as a FastAPI Response with the correct media type
    # return Response(content=map_html, media_type="text/html")
    return "hola mono"

@app.post("/clickCoords")
async def get_coords(request: Request):
    data = await request.json()
    lat = data.get("lat")
    lng = data.get("lng")
    print(f"Coordenadas recibidas: Latitud={lat}, Longitud={lng}")
    # Aquí puedes hacer lo que necesites con las coordenadas
    return {"message": f"Coordenadas ({lat}, {lng}) recibidas exitosamente"}

@app.get("/coord/{coord_A}/{coord_B}") # -33.337528338594026/-66.30829314167931
def get_coords(coord_A:float ,coord_B:float):
    #paso las coordenadas del mapa
    lat = coord_A
    lon = coord_B
    mapa = folium.Map(location=[lat, lon], zoom_start = 15, min_zoom = 10, max_zoom = 17, 
            tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community')

    # Add a marker to the map (optional)
    folium.Marker([-33.32532966247154, -66.307608038267], icon=folium.Icon(color='red', con_color="black"), popup="Mi Casa").add_to(mapa)

    # Añade un marcador
    folium.Marker(
        location=[-33.344976308695585, -66.26681749851481],
        popup='Piedras raras',
        icon=folium.Icon(icon="camera", color="red", con_color="black", iprefix="fa") # con_color="black", 
    ).add_to(mapa)

    # Inject JS inside the html generated

    script = """
    <script>

        function clickBody() {

        console.log("Hola Mono!");
        }
        document.addEventListener("click", clickBody)

    </script>
    """

    mapa.get_root().html.add_child(folium.Element(script))
    
    map_html = mapa._repr_html_()

    # Return the HTML as a FastAPI Response with the correct media type
    return Response(content=map_html, media_type="text/html")

