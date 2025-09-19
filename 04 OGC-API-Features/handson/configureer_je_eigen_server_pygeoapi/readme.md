# Configureer je eigen server met pygeoapi

pygeoapi is een python server implementatie van de OGC API standaarden.

Zie [pygeoapi.io](https://pygeoapi.io/) voor alle documentatie en informatie.

Een hele mooie manier om met verschillende software oplossingen te experimenteren is via Docker

Zie [Docker Desktop](https://docs.docker.com/desktop) voor informatie over de installatie daarvan. 
```
Docker Desktop is free for:
Small businesses (fewer than 250 employees AND less than $10 million in annual revenue)
Personal use
Education
Non-commercial open source projects
```

Als je docker (en docker compose) geinstalleerd hebt zou je op de commandline de volgende commando's moeten kunnen uitvoeren en een versienummer terug krijgen:
```
docker version
docker compose version
```

### docker compose

Docker compose is een commando om een docker container te configureren.
Dit commando leest de ```docker-compose.yml``` file en maakt een container aan op basis van die configuratie file.

```
pygeoapi:
    image: geopython/pygeoapi:latest

    container_name: pygeoapi

    ports:
      - 5000:80

    volumes:
      - ./pygeoapi.config.yml:/pygeoapi/local.config.yml
      - ./data:/data
```
De compose file beschrijft een aantal dingen.

1) __image:__ welk basis image gebruikt moet worden. in dit geval ```geopython/pygeoapi:latest``` Dit is een docker image wat door de makers van pygeoapi beschikbaar gesteld wordt en wat je zo kunt gebruiken.
2) __ports:__ Dit verteld welke poort er vanuit de container (80) beschikbaar gesteld moet worden op de host (je computer) (5000)
3) __volumes:__ Dit verteld welke mappen of bestanden van je host computer beschikbaar moeten worden in de container.
    
    Dus de ```pygeoapi.config.yml``` die in deze folder staat komt tevoorschijn in de container als ```/pygeoapi/local.config.yml``` 
    en de folder ```data``` komt in de container beschikbaar als folder ```data``` 
    
    Het docker image is zo gebouwd dat deze 'luistert' naar een configuratiefile in de /pygeoapi folder genaamd local.config.yml

### pygeoapi configuratie

De ```pygeoapi.config.yml``` beschrijft hoe de pygeoapi server geconfigureerd moet worden. Hier staan ook weer een paar belangrijke onderdelen in. Voor de volledige documentatie kun je bij pygeoapi.io terecht.

1) 
```
server:
    bind:
        host: 0.0.0.0
        port: 5000
```
Dit stuk verteld op welke poort de pygeoapi server moet werken. Dit moet dus overeenkomen met de poort configuratie in de docker-compose.yml

2) resources:
```
providers:
            - type: feature
              name: GeoJSON
              data: /data/knmi_meetstations.geojson
              id_field: STN
```
__type__ verteld wat voor soort OGC API Service het moet zijn (feature in dit geval)

__name__ verteld het formaat van het geodata bestand

__data__ verteld de locatie van het bestand (in het geval van een bestand, zie de pygeoapi documentatie voor bijvoorbeeld database connecties etc.) De locatie hier (/data) moet overeenkomen met de volumes mapping in de docker-compose configuratie.

---

Via ```docker compose up``` vertel je docker om de container op te starten. In de terminal zie je dat de server gestart wordt. Als het goed gaat zie je dat de openapi.yml gegenereerd wordt en de server start. Dan kun je in de browser naar http://localhost:5000

---
Oefening:

Probeer eens nieuwe lagen toe te voegen. Er staat meer data in de data folders van de bouw_je_eigen_server.

De metadata van de buurten geojson geeft nu heel Nederland als extent. Hoe zou je dat kunnen verbeteren?

Probeer je lokale server ook uit in een van de andere handson oefeningen. (webclient, GIS)
