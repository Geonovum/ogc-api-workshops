# Oefening 4: Gebouwen tellen per gebied

## Doel
Statistische analyse.

## Wat leer je?
- `COUNT`
- `GROUP BY`

## Query

```sparql
prefix imxgeo: <http://modellen.geostandaarden.nl/def/imx-geo#>
SELECT ?woonplaats (COUNT(?gebouw) as ?aantal) 
WHERE {
  ?gebouw a imxgeo:Gebouw ;
    imxgeo:bevindtZichOpPerceel/imxgeo:ligtInRegistratieveRuimte ?woonplaats.
  ?woonplaats a imxgeo:Woonplaats;
    imxgeo:naam ?naam. 
    
}
GROUP BY ?woonplaats
ORDER BY DESC(?aantal)
```

## Opdrachten
1. Toon alleen woonplaatsen met meer dan 100 gebouwen.
2. Maak een top 10.
