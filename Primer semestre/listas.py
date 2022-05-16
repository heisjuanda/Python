num="12"
num1="10"
re=num+num1
print(re)
converint=int(num1)+ int(num)
print(converint)
print("-----------------------------------------")
edad=int(input("digite su edad"))
nombre=str(input("digita tu nombre"))
print("tú "+ nombre + ", tienes " + str(edad) + " años de edad")
print("----------------------------------------")
#listas, en ellas exite cualquier cosa
lista=[1,2,3,4,5]
lista1=[1,2.4,"hola pa",[5,3],4]
print(lista)
print(lista1)
#para acceder hay que hacer
print(lista1[3][1])
print(lista1[2][1])
print(lista1[2][0:4])#rango en listas para sacar cosas
#for
lista2=[1,2,3,4,5,6,6]
for element in lista2:
    print(element)
print("------------------------")
lista2.append(9)#se agrego el nueve a la lista
print(lista2)
lista2.extend([3,5])#agrega una lista o otra  
print(lista2)
lista2.remove(9)#quita elemento de la lista
print(lista2)
print(lista2.index(1))#saca el posicionamiento del valor
print(lista2.count(3))#cuenta las veces que se repite algo
lista2.reverse()#lista al reves
print(lista2)
print("-----------")
lista3=[1,2.5,'lista',[5,6],4,5,3.2,5]
dialista=["lunes","martes","miercoles","jueves","viernes"
          "sábado","domingo"]
lista3.extend([2,3,4])
lista3.remove(3)
print(lista3.count(2))
lista3.reverse()
print(lista3)



