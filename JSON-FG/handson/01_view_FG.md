# View JSON-FG examples in a browser or JSON-editor

In this exercise you will learn to recognise the new elements of JSON-FG
You will need a text editor like Notepad++ or Visual Studio, preferable one that recognises JSON file structures.

## Step 1 download files

Download the JSON-FG examples from ./data/FG_data

## Step 2 CRS

- Open crs_BGT_FG.json in a text editor.
Notice the combined use of the place and geometry element. What is the difference between these 2 elements?

- Also view the PDOK API for the BGT in your browser: https://api.pdok.nl/lv/bgt/ogc/v1/collections/pand/items.

- Click on "JSON-FG" in the top right to view the JSON-FG response.

- Go back to https://api.pdok.nl/lv/bgt/ogc/v1/collections/pand/items

- Now choose a different CRS, e.g. http://www.opengis.net/def/crs/EPSG/0/28992 (RD), and then click on "JSON-FG" again. What is the difference?

## Step 3 Time

Open time_communities_NL_FG.json in a text editor. 
Locate the time element.

## Step 4 3D

Open 3D_polyhedron_dom_FG.json and 3D_prism_toronto-city-hall in a text editor. 
Notice the difference in structure for 3D.

## Step 5 Curves

Open curves_FG.json in a text editor.
Find the 3 new datatypes:  CircularString, CompoundCurve and Curve Polygon

## Step 6 Measures

Open measures_road-segment_FG.json in a text editor.
What is the unit of measures? 