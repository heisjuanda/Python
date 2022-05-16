
# Online Python - IDE, Editor, Compiler, Interpreter

def s(z):
  if z ==0:
   return 0 
  return z+s(x-1)
def asa():
    print(v+1,end='')
v=1 
asa() 
print(v)

def a(x,b):
    return x**x
#print(a(2))  

d={'one':'two','three':'one','two':'three'}
v=d['one']
l=['a','b','c','d']
for i in range(len(d)):
   v=d[v]
print(v,"juanda")   
for i in sorted(d.keys()):
    k = d[i]
    print(k[0])    
tup = (1,2,4,8)
tup= tup[1:-1] 
tup=tup[0]
print("asd",tup)

def any(x):
   global y
   y= x*x
   return y
any(2)   
print("globla",y)
   
x=2 
x=any(x+1)
print(x)



try:
    v=2
    print(v/v)
except ValueError:
    print("entrada incorrecta")
except TypeError:
    print("s")
except ZeroDivisionError:
    print("p")















vals=[3,1,-2]
print(vals[vals[-1]])

for i in range(len(vals)):
    vals.insert(1,vals[i])

print(vals)
x=1 
x=x==x 
print(x)
a=1 
b=0
c=a&b 
d=a|b 
print(c+d)

a=1
while a<10:
    print("op")
    a=a<<1

my_list = [1,2,3,4]
print(my_list[-3:-2])

t=[[3-i for i in range(3)]for j in range(3)]
s=0 
for i in range(3):
    s+=t[i][i]

z=10
y=0
x = y<z and z>y or y>z and z<y 
print(s)

