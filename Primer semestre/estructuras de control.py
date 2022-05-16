#estructuras de control
variable=5
if variable>10:
    print("varible es mayor")
else:
    print("variable es menor")
#print("siempre se muestra")   
print("---------------------")
#elif=contradice el else
variables=3
if variables>3:
    print("varibles es mayor")
elif variables<3:
    print("la variables es menor")
else:
    print("la variable es igual")
print("------------------------")
#while
print("estepar")
a=0
while a<10:
    a=a+2
    print(a)
print("esteimpar")    
b=1    
while b<10:
    b=b+2
    print(b)
print("esteadormir")    
w=0    
while w <10:
    w=w+1
    if w==3:
        break
    print(w)
print("----------------------")
primero = 3

while primero<=10:
		print ("Tabla del " + str(primero))
		segundo=1
		while segundo<=10:
			print (str(primero)+ "X" + str(segundo)+"="+ str(primero*segundo))
			segundo+=1
		primero +=1
		print ("\n")
print ("Se termino")












