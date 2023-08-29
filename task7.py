'''#task1
def even_checker(a):
  if a%2!=0:
    print("Odd!!")
  else:
    print("Even!!")
even_checker(4)'''

'''#task2
def fibonacci(a):
  max=a
  b=0
  c=1
  sum=1
  print(0,end=" ")
  while sum<=max:
    print(sum,end=" ")
    sum=b+c
    b=c
    c=sum
fibonacci(10)'''

'''#task3
def foo_moo(a):
  if a%2==0 and a%3==0:
    return("FooMoo")
  elif a%2==0:
    return("Foo")
  elif a%3==0:
    return("Moo")
  else:
    return("Boo")
foo_moo(5)'''

'''#task5
a=int(input())
b=int(input())
c=input()
def calculate_tax(a,b,c):
  if a<18 or c=="President" or b<10000:
    return(0)
  elif 10000<=b<=20000:
    return(b*0.05)
  elif b>20000:
    return(b*0.1)
calculate_tax(a,b,c)'''

'''#task6
a=int(input())
def calander(a):
  month=(a%365)//30
  year=a//365
  days=(a%365)%30
  print(f'{year} years, {month} months and {days} days')
calander(a)'''

'''#task7
def show_palindrome(a):
  for i in range(1,a,1):
    print(i,end="")
  for i in range(a,0,-1):
    print(i,end="")
show_palindrome(5)'''

'''#task8
def show_palindromic(a):
  s=""
  for i in range(1,a+1):
    s+=str(i)+" "
  for i in range(a-1,0,-1):
    s+=str(i)+" "
  print(s)
#for space
def show_palindromic_triangle(a):
  for i in range(1,a+1):
    for j in range(0,a-i):
      print(" ",end=" ")
    show_palindromic(i)
show_palindromic_triangle(5)'''

"""#task9
import math
def area_circumference_generator(a):
  area=math.pi*a**2
  cir=2*math.pi*a
  d=(area,cir)
  return(d)
ad=area_circumference_generator(1)
x,y=ad
print(ad)
print(f'Area of the circle is {x} and circumference is {y}')"""


'''#task10
def make_square(a):
    b={}
    start,end=a
    for i in range(start,end+1):
        b[i]=i**2
    print(.b)    
make_square((2,5))'''

'''def rem_duplicate(a):
  lst=[]
  for i in a:
    if i not in lst:
      lst.append(i)
  print(tuple(lst))
rem_duplicate(("Hi", 1, 2, 3, 3, "Hi",'a', 'a', [1,2]))'''

'''#task12
def lis(a):
    l = []
    c = 0
    for elements in a:
        if l.count(elements) < 2:
            l.append(elements)
        else:
            c += 1
    print(f"Removed: {c}")
    print(l)
lis([1, 2, 3, 3, 3, 3, 4, 5, 8, 8])
'''

'''#task13
a=input("what do you want ")
b=float(input("first call "))
c=float(input("Second call "))
def calc(a,b,c):
    re=0
    if "+" in a:
        re=b+c
    elif "-" in a:
        re=b-c
    elif "/" in a:
        re=b/c
    elif "*" in a:
        re=b*c
    else:
        print("error404")
    print(re)
calc(a,b,c)
'''

'''#task14
a=input()
b=int(input())
def random(a,b):
  x=a[0]
  y=""
  for i in range(1,len(a)):
    if i%b!=0:
      x+=a[i]
    else:
      y+=a[i]
  z=x+y
  return(z)
random(a,b)'''

#task15
def cart(a,location="Dhanmondi"):
  menu={"Rice":105,"Potato":20,"Chicken":250,"Beef":510,"Oli":85}
  pac=0
  for i in a:
    pac+=menu[i]
  if location=="Dhanmondi":
    pac+=30
  else:
    pac+=70
  print(pac)
cart(["Rice", "Beef", "Rice"], "Mohakhali")