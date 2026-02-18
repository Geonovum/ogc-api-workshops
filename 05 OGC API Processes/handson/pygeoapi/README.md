# PygeoAPI Demo server

Starten met `docker compose up`

- pygeoapi.config.yml is de configuratie file die, samen met de plugins/process en /data folder gemapt zijn naar de docker container.

als de container gestart is, is de server te benaderen op http://localhost:5000/

---
pygeoapi publiceert een docker image. In deze folder is een eigen dockerfile gedefinieerd op basis van dit image omdat een van de processes aanvullende python packages vereist.

#### client.ipynb

Dit is een Jupyter Notebook waarmee de Pygeoapi OGC API Processes aangeroepen worden.

Benodigde packages:
- jupyter notebook
- requests
- json
- geopandas
- folium (voor de kaartjes, zonder kan evt ook)

---
disclaimer: configuratie van Pygeoapi en het client notebook zijn ten behoeve van demonstratie en leerdoeleinden. Zeker niet geschikt om een productie installatie mee te doen!