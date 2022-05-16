#edad de una persona clasificación
edad=int(input("digite la edad"))
if edad>=0 and edad<=5:
   print("es un bebe")
else:         
  if edad>=6 and edad<=12:
      print("es niño todavía")
  else:
      if edad>=13 and edad<=17:
          print("es un adolescente")
      else:
          if edad>=18:
              print("es un adulto")
     
