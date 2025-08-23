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
    folium.Marker([-37.272754406138894, -56.97811560712071], icon=folium.Icon(color='green'), popup="Mi Casa").add_to(mapa)

    # Añade un marcador
    folium.Marker(
        location=[-37.27248159475287, -56.9781009466294],
        popup='Lo de Tarzan',
        icon=folium.Icon(color='blue')
    ).add_to(mapa)

    map_html = mapa._repr_html_()

    # Return the HTML as a FastAPI Response with the correct media type
    return Response(content=map_html, media_type="text/html")