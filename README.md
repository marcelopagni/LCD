Servidor + Docs / API en python con FastAPI

DDBB MySQL

POSTMAN para ir testeando la API, luego se pensara en la mejor opción para el cliente

=====================================================================================
Primo:

- Hace un **git status** en el directorio de la app, desde la terminal de git, y te va a tirar que esta desactualizado tu local
- Tirale un **git fetch** y te va a decir cuales son los archivos o directorios desactualizados
- Despues un **git pull** y ahi te baja la actualizacion en el local
- Apaga el Docker por las dudas, y en el directorio LCD mandale el comando **docker compose build** para recrear la imagen
- Y despues siempre desde la terminal corré **docker compose up**
- Fijate en **localhost:8000/docs** la documentación autogenerada por swagger, ahí te va a marcar una nueva que es **/mapa**
- En **localhost:8000/mapa** fijate que está el mapa mas el shp de la geometría de los afloramientos rocosos, que se yo es un archivo de prueba
