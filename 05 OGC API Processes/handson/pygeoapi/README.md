# PygeoAPI Demo server voor OGC API Processes

## Server 

Benodigd: Docker (Desktop)

Start de demo met het commando `docker compose up` op de commandline/terminal

- pygeoapi.config.yml is de configuratie file die, samen met de plugins/process en /data folder gemapt zijn naar de docker container.

als de container gestart is, is de server te benaderen op http://localhost:5000/

---
pygeoapi publiceert een docker image. In deze folder is een eigen dockerfile gedefinieerd op basis van dit image omdat een van de processes aanvullende python packages vereist.

## Client

Omdat er (nog) geen standaard ondersteuning in pakketten zoals QGIS is, bevat deze demo een Client op basis van een Jupyter Notebook.

### Optie 1

Als je al een python omgeving (met jupyter) op je machine hebt kun je __client.ipynb__ openen

Dit is een Jupyter Notebook waarmee de Pygeoapi OGC API Processes aangeroepen worden.

Benodigde packages:
- jupyter notebook
- requests
- json
- geopandas
- folium (voor de kaartjes, zonder kan evt ook)

### Optie 2

Als je geen python op je laptop beschikbaar hebt.

In plaats van de server starten met ```docker compose up``` (zoals hierboven staat) kun je de server in combinatie met een jupyternotebook server starten met: ```docker compose -f docker-compose-jupyter.yml up```. 

Op de commandline zie je de logging langskomen van de pygeoapi server en de jupyter server die gestart worden. In de logregels van jupyter komt op een gegeven moment een url langs in de vorm van ```http://127.0.0.1:8888/lab?token=<token>``` gebruik deze url om de jupyter lab omgeving te openen.

In de jupyter lab omgeving (in je browser) kun je aan de linkerkant de `work` folder openen en daarin staat het `docker-client.ipynb` notebook. 

---
disclaimer: configuratie van Pygeoapi en het client notebook zijn ten behoeve van demonstratie en leerdoeleinden. Zeker niet geschikt om een productie installatie mee te doen!