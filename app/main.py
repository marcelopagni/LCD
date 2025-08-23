from fastapi import FastAPI, Response

import folium

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a la aplicación del Cuaderno de Campo Digital!"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    # Lógica para obtener el item_id de la base de datos
    return {"item": f"Elemento con ID {item_id}"}


@app.get("/coord/{coord_A}/{coord_B}")
def get_coords(coord_A:float ,coord_B:float):
    #paso las coordenadas del mapa
    lat = coord_A
    lon = coord_B
    mapa = folium.Map(location=[lat, lon], zoom_start = 15)

    # Add a marker to the map (optional)
    folium.Marker([-33.32532966247154, -66.307608038267], icon=folium.Icon(color='green'), popup="Mi Casa").add_to(mapa)

    # Añade un marcador
    folium.Marker(
        location=[-33.33588710719352, -66.30433207219897],
        popup='Lo de Tarzan',
        icon=folium.Icon(icon="home", color="purple", icon_color="blue", prefix="fa")
    ).add_to(mapa)

    map_html = mapa._repr_html_()

    # Return the HTML as a FastAPI Response with the correct media type
    return Response(content=map_html, media_type="text/html")