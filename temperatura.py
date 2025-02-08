temperatura= []
for n in range (0,5):
  t= int(input("ingrese la temperatura "))
  temperatura.append(t) 
promedio = sum( temperatura)/len(temperatura)
print("la temperatura esta perfecta:",promedio)
if temperatura < 20 :
  print("necesita una revision")
elif 20>= promedio <=30:
  print("la temperatura esta perfecta")
else:
  print("es necesaria una revision de los conctos de aire")
      


 