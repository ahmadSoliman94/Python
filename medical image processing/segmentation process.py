import SimpleITK as sitk
import sys
from image_viewing import * 

# Main-Methode: Der Bennutzer muss die Eingabe, Ausgabe, gegebene Segmentierung und die Saatpunkte der Achsen (x,y,z) selbststaendig in die Console eingeben.
# Es sind 6 Eingaben erforderlich
if __name__ == '__main__':
    if len(sys.argv) < 6:
        print('Usage: python ' + str(sys.argv[0]) + ' <input filename> <output filename> <OT_reg filename> <seedX> <seedY> <seedZ>')
        exit(-1)

# Die Sequenz wird gelesen von der Console (argv)
reader = sitk.ImageFileReader()
reader.SetFileName(sys.argv[1])
input_image = reader.Execute()
show_image(input_image, 'Input Image', blocking=False) # Ausgabe des Eingabebildes (Sequenz FLAIR)

# Die gegebene Segmentierung wird gelesen und ausgegeben, damit wir diese mit unserer Segmentierung vergleichen können (für Dice-Koefficient).
reader = sitk.ImageFileReader()
reader.SetFileName(sys.argv[3])
OT_reg = reader.Execute()
#show_image_with_mask(input_image, OT_reg, 'ot', color='b',blocking=False) # Ausgabe des Eingabebildes (OT_reg)


# Glättungsverfahren
clurFilter = sitk.CurvatureFlowImageFilter()
clurFilter.SetNumberOfIterations(2) # Anzahl der Wiederholungen des Glättungsverfahren
clurFilter.SetTimeStep(0.250)
smoothed = clurFilter.Execute(input_image)
show_image(smoothed, 'Smoothed', blocking=False) # Das geglätete Bild wird angezeigt


# Saatpunkte eingeben in die Console
seedX = int(sys.argv[4])
seedY = int(sys.argv[5])
seedZ = int(sys.argv[6])

# Die Anzahl der nächsten Saatpunkte werden automatisch betrachtet
seedpoint = [seedX, seedY, seedZ]
print(seedpoint)
seed = []
count = 0
for x in range(0, 25): # Anzahl der Saatpunkte für die x-Achse
    seedpoint = (seedX+x, seedY, seedZ)
    count += 1
    seed.append(seedpoint)
for y in range(0, 25): # Anzahl der Saatpunkte für die y-Achse
    seedpoint = (seedpoint[0], seedY+y, seedZ)
    count += 1
    seed.append(seedpoint)
print("seedPoints: ", seed)

# Segmentierung
segmentation = sitk.ConfidenceConnectedImageFilter() 
segmentation.SetSeedList(seed)
segmentation.SetMultiplier(0.3) # Anzahl der Multiplikator festlegen, um das Konfidenzintervall zu definieren. 
segmentation.SetInitialNeighborhoodRadius(3) # Anzahl der Radien der Nachbarschaften
seg = segmentation.Execute(smoothed)


# Closing-Verfahren zum Schließen der Lücken
vector = (10, 10, 10) # Intervall für die Achsen (x,y,z) 
kernel = sitk.sitkBall 
morphologicalClosing = sitk.BinaryMorphologicalClosing(seg, vector, kernel)


# Dice Coefficient Berechnung
overlap = sitk.LabelOverlapMeasuresImageFilter()
overlap.Execute(OT_reg, morphologicalClosing) # Die gegebene Segmentierung wird von der Segmentierung subtrahiert
print("\nDiceCoefficient:", overlap.GetDiceCoefficient())

# Volumen Berechnung
labelShape = sitk.LabelShapeStatisticsImageFilter() 
labelShape.Execute(morphologicalClosing)
getLabel = labelShape.GetLabels() # Ein Wert der in der Execute-Methoden aktuallisiert wird und erst nach der Ausführung gültig ist.
for label in getLabel: # Physikalische Größe für alle Werte
    volume = labelShape.GetPhysicalSize(label)
print("Lesion volume: ", volume,  "mm3")



# Ausgabe von der verarbeiteten Segmentierung
show_image_with_mask(input_image, morphologicalClosing, 'Result', color='r')

# Ausgabebild wird gelesen
writer = sitk.ImageFileWriter()
writer.SetFileName(sys.argv[2])
writer.Execute(morphologicalClosing)
