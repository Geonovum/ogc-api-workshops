# Create BGT_FG file with curve

In this exercise you will learn the advantage of using the circular string and compound curve 
You will need QGIS and a text editor like Notepad++ or Visual Studio, preferable one that recognises JSON file structures.

## Step 1 Inspect the PDOK OGC-API-Features

- Go in your internet browser to https://api.pdok.nl/lv/bgt/ogc/v1/collections/ondersteunendwegdeel/items 
- Set it to the CRS with http://www.opengis.net/def/crs/EPSG/0/28992
- Ask for Lokaal_id: G0307.92a82176fc034ee7a74f26870f34e44c.
- Press "Filters toepassen" and you will see a small supporting road part (ondersteunendwegdeel) with circular shape.
- Press "JSON-FG" in the top-right menu. This must be a disappointment.

## Step 2 create your own JSON-FG

- download the JSON-FG file from the browser
- make a copy.
- open the copied file in a text-editor
- edit the file by replacing the stroked curve with a and compound curve containing one circular string and one line string (see also slide 19 in presentation) 
- save the file and compare the size with the downloaded file
- open both files in QGIS (first do exercise 03_load_FG_QGIS.md if you're not experienced with QGIS) and compare them by zooming in strongly.