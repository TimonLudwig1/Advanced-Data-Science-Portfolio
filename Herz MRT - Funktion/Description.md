**Cardiac MRI - Function**
***Challenge description:***

A cardiac MRI examination typically includes a so-called Cine acquisition. The heart is 
imaged across multiple layers (slices) and at different time points throughout the cardiac 
cycle (frames).

From the Cine data, important information about cardiac function can be derived. One such 
measure is the ejection fraction — the proportion of blood volume that is pumped out of 
the left ventricle with each heartbeat.

The task is to calculate the ejection fraction for the provided dataset. The data comes 
from the Data Science Bowl Cardiac Challenge dataset on Kaggle. The folder data/manual 
contains images that provide a pixel-accurate segmentation for each image in data/images, 
classifying each pixel as background (0), left ventricle (1), or heart muscle (2). To 
calculate the ejection fraction, proceed as follows:

1. Count the pixels belonging to the left ventricle for each image in data/manual.
2. Sum these pixel counts across all slices for each time point.
3. The time point with the largest sum corresponds to diastole.
4. The time point with the smallest sum corresponds to systole.
5. The ejection fraction is calculated as 1 - Pixel(Systole) / Pixel(Diastole).

Give your answer as a percentage, rounded to two decimal places, e.g.: 62.19%.

Note: When viewing the images in data/manual or data/auto with a standard image viewer, 
they appear completely black. This is because the pixel values 0, 1, and 2 (out of 255) 
are all extremely dark.

This challenge was created by the Chair of Cellular and Molecular Imaging at the German 
Centre for Cardiovascular Research.

***Beschreibung der Challenge deutsch:***

Zu einer MRT Untersuchung des Herzens gehört in der Regel eine sogenannte Cine Aufnahme. Dabei wird das Herz in verschiedenen Schichten (slices) und zu verschiedenen Zeitpunkten im Herzzyklus (frames) aufgenommen. 

Aus den Cine Daten kann man wichtige Informationen über die Herzfunktion berechnen. Ein solcher Wert ist die Ejektionsfraktion also der Anteil des Blutvolumens der bei einem Herzschlag aus der linken Kammer ausgeworfen wird.

Die Aufgabe ist es für den hier zur Verfügung gestellten Datensatz die Ejektionsfraktion zu berechnen. Die Daten stammen aus dem Data Science Bowl Cardiac Challenge Datensatz von Kaggle. Im Ordner data/manual befinden sich Bilder, die für jedes Bild in data/images eine pixelgenaue Einteilungen in Hintergrund (0), linke Herzkammer (1) und Herzmuskel (2) vorgeben. Um die Ejektionsfraktion zu berechnen können Sie so vorgehen:

Zählen Sie für jedes Bild in data/manual die Pixel die zur linken Herzkammer gehören.
Summieren Sie für jeden Zeitpunkt diese Pixelwerte über alle Schichten hinweg.
Der Zeitpunkt mit der größten Summe ist die Diastole.
Der Zeitpunkt mit der kleinsten Summe ist die Systole.
Die Ejektionsfraktion berechnet sich als 1-Pixel(Systole)/Pixel(Diastole)
Geben Sie die Antwort in Prozent, gerundet auf zwei Stellen nach dem Komma, z.B.: 62.19%.

Hinweis: Wenn man sich die Bilder in data/manual oder data/auto mit einem normalen Imageviewer ansieht, sehen die Bilder einfach schwarz aus. Das liegt daran, dass die Pixelwerte 0, 1 und 2 (von 255) alle sehr dunkel sind.

Diese Challenge wurde vom Lehrstuhl Zelluläre und Molekulare Bildgebung des Deutschen Zentrums für Herzinsuffizienz erstellt.