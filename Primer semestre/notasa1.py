cantidadNotas = int(input("Digite la cantidad de notas:  "))
suma = 0.0


for i in range(cantidadNotas):
       nota = float(input("Digite la nota #"+ str(i+1) +":" ))
       suma+=nota
      

promedio = suma / cantidadNotas

print("El promedio es: " + str(promedio))
      
    

   
