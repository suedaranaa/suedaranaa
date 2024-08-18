
#Öklid Mesafesi Hesaplama Python



import math

def points():
    points = []
    n=int (input("İstediğiniz çift nokta sayısını giriniz: "))
    
    for i in range(n):
        x = float(input(f"{i+1}. noktanın x koordinatlarını girin: "))
        y = float(input(f"{i+1}. noktanın y koordinatlarını girin: "))
        points.append((x,y))
        return points
    
def Distancee(point1,point2):
    x1,y1=point1
    x2,y2=point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

points = points()
distancees = []



for i in range(len(points)):
           for j in range(i+1,len(points)):
               distancees=Distancee(points[i],points[j])
               distancees.append(distancees)
               
if distancees:
    minDistancee=min(distancees)
    print(f"min mesafe: {minDistancee}")
else :
    print("Daha fazla nokta çifti giriniz.")

#şu an hata alıyorum ama düzelteceğim.

