# Time slider in QGIS

In this exercise you will learn how to use the time element of JSON-FG files in QGIS and create a time slider showing the changes of the community borders in the Netherlands. 

## Step 1

Go to "Databronnen beheren" in QGIS (Ctrl+L) and browse to the folder where the JSON-FG sample files were downloaded.
Select time_communities_NL_FG.json and click "Toevoegen".
Select item "gemeentes"
Select the first CRS tranformation option.
If all goes well, the Dutch communities will appear.

## Step 2

In the list of layers You can right click the just added layer and select "eigenschappen" (properties).
Go to "Tijdbeheer" (time settings)
Select for "Dynamisch Tijdbeheer"
Select Configurarie "Afzonderlijke veldenvoor start en einde Datum/Tijd" (Separate fields for start and end Date/Time)
Select Limieten "Inclusief Start, exclusief Einde (standaard)" (Includes Start, excludes End (standard))
Select the fields for "Start" and "Einde" (end)
click "OK"

## Step 3

Click in the main menu on "beeld" (view/display?) and "panelen" (panels) and select "Tijdbeheer" (time settings)
Select "Geanimeerde navigatie voor tijd" (Animated navigation for time)
Set range to "Volledig bereik instellen" (full range) 
Set Stap to 6 maanden (6 months)

Now, you can play the animation and see the amount of communities reduce.

##Step 4

improve the animation by dubbel clicking on the layer and setting a symbolygy on "Categoriën" with Waarde (Value) equal to "jsonfg_time_end"