# Time slider in QGIS

In this exercise you will learn how to use the time element of JSON-FG files in QGIS and create a time slider showing the changes of the community borders in the Netherlands. 

## Step 1

Go to "Databronnen beheren" (Data Source Manager) in QGIS (Ctrl+L) and browse to the folder where the JSON-FG sample files were downloaded.
Select time_communities_NL_FG.json and click "Toevoegen" (Add Selected Layers).
Select item "gemeentes"
Select the first CRS transformation option.
If all goes well, the Dutch communities will appear.

## Step 2

In the list of layers you can double click the just added layer to edit the properties.
Go to "Tijdbeheer" (Temporal).
Select for "Dynamisch Tijdbeheer" (Dynamic Temporal Control).
Select Configuratie "Afzonderlijke velden voor start en einde Datum/Tijd" (Separate Fields for Start and End Date/Time)
Select Limieten "Inclusief Start, exclusief Einde (standaard)" (Include Start, Exclude End (default))
Select the "begingeldigheid" and "eindgeldigheid" fields as Start field and End field.
Click "OK"

## Step 3

Click in the main menu on "beeld" (View) and "panelen" (Panels) and select "Tijdbeheer" (Temporal Controller)
Click the "Geanimeerde navigatie voor tijd" (Animated temporal navigation) button.
Click the "Volledig bereik instellen" (Set to Full Range) button. 
Set Stap to 6 maanden (Step: 6 months).

Now, you can play the animation and see the number of communities reduce.

##Step 4

Improve the animation by double clicking on the layer and by setting a symbology on "Categoriën" (Categorized) with Waarde (Value) equal to "begingeldigheid" (or "eindgeldigheid").