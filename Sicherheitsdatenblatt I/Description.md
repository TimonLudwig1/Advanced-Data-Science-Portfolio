**Safety Data Sheet**
***Description***

A Safety Data Sheet (SDS) contains information about the hazards of chemical substances 
or products. SDSs follow a standardized structure — for example, they always consist of 
16 sections with nearly standardized heading text.

The goal is to automatically extract the trade name / product name / product identifier 
from Section 1 of each SDS. For this purpose, several SDSs are provided as PDF files. 
To simplify processing, the text sections have already been extracted from each PDF. 
These text sections are provided in a CSV file along with their X and Y positions.

The task is to write code that finds and outputs the trade name for each SDS. For 
example, for 'orangenoelReiniger' the output should be 'Muster-GeSi-Reiniger Orange, 
Konzentrat'.

The solution is the concatenation of all 25 names, sorted by filename, separated by 
semicolons, and without any additional whitespace. For example:
Trade Name 1;Long Name with - Minus - and Number 2;ShortName;...

Hint: Start by sorting the text sections from the CSV file into a meaningful order.

This challenge was created by GeSi Software GmbH.

***Beschreibung***

Ein Sicherheitsdatenblatt (SDB) enthält Information über Gefahren chemischer Stoffe oder Produkte. SDBs sind nach einem vorgegebenen Schema aufgebaut, so bestehen sie z.B immer aus 16 Abschnitten mit nahezu standardisiertem Überschriftstext.

Wir wollen im Folgenden den Handelsnamen/Produktnamen/Produktidentifikator aus Abschnitt 1 automatisiert einlesen. Dafür haben wir einige SDBs als PDF-Datei gegeben, zur Vereinfachung wurden die Textabschnitte bereits aus der jeweils zugehörigen PDF-Datei extrahiert. Diese Textabschnitte werden mit ihrer X und Y-Position in einer CSV-Datei gegeben.

Gefordert ist ein Code, der für jedes der SDBs den Handelsnamen findet und ausgibt. So soll für 'orangenoelReiniger' etwa 'Muster-GeSi-Reiniger Orange, Konzentrat' ausgegeben werden.

Die Lösung ist die Verkettung aller 25 Namen, sortiert nach Dateinamen, getrennt durch Semikolon und ohne zusätzliche Leerzeichen. Also z.B. Handelsname 1;Langer Name mit - Minus - und Zahl 2;Kurzername;...

Tipp: Sortieren Sie zunächst die Textabschnitte aus der CSV-Datei in einer sinvollen Reihenfolge.

Diese Challenge wurde von der GeSi Software GmbH erstellt.