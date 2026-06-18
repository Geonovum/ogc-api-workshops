# Load JSON-FG files in QGIS

In this exercise, you will learn how to load a JSON-FG file in QGIS and experience the new data types for CircularString, CompoundCurve, and CurvePolygon.

## Step 1

Open QGIS and check if the version number is greater than or equal to 3.44.
If the version number is lower, it is possible that JSON-FG is not yet properly supported.
If necessary, download a newer version via: https://www.qgis.org/nl/download/

## Step 2

Go to "Databronnen beheren" in QGIS (Ctrl+L) and browse to the folder where the JSON-FG sample files were downloaded.
Select curves_FG.json and click "Toevoegen".
If all goes well, a polygon with three holes will appear. If necessary, add an extra layer from the browser via a WMS/WMTS connection for orientation, such as an aerial photo mosaic from https://service.pdok.nl/hwh/luchtfotorgb/wmts/v1_0?request=GetCapabilities&service=wmts
Try to find the elements from the JSON-FG file.
