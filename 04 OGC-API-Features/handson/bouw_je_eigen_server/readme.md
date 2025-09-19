# Bouw je eigen OGC API Features server

In het stappenplan in deze folder leer je hoe je met wat basis javascript een eigen server kunt bouwen.

Let op, dit is natuurlijk geen productie code maar puur bedoelt om inzicht te geven in de onderliggende principes hoe een OGC API Features server werkt.


## Benodigdheden

- Visual Studio Code

We gebruiken vscode (https://code.visualstudio.com/) als editor om deze tutorial te doen. Installeer de geschikte versie voor jouw OS.

- node en npm

> Node.js® is a free, open-source, cross-platform JavaScript runtime environment that lets developers create servers, web apps, command line tools and scripts.

We coderen de server met Node en npm. Installeer de laatste LTS versie voor jouw OS: https://nodejs.org/en

- Bruno 

We gebruiken de browser, en [Bruno](https://www.usebruno.com/) om de server te bevragen. Bruno is een open source API client. (maar als je een andere API client wilt gebruiken kan dat natuurlijk ook)

- De OGC-API-WORKSHOPS Git repository (deze repo)

Download of clone deze [repo](https://github.com/Geonovum/ogc-api-workshops),
dat kan met de git functionaliteit in VS Code.

Open vervolgens de repository in VS Code.

De stappen in de tutorial zijn geschreven de Bart de Lathouwer.

Elke stap legt een volgend stukje uit.
- basis werking van een webserver
- HTTP methods (GET, POST, ...)
- routes (/collections, /collections/{id}, ...)
- content negotiation (HTML, JSON)

Elke stap/folder werkt op zichzelf. De werking van de server in stap9 is dus niet afhankelijk van de stappen ervoor.

## Stap 1

Klaar voor [Stap1](./stap1/readme.md)!