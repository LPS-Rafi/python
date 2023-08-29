"""#task1
    #a
print("a)",end=" ")
for i in range(24,-7,-6):
    if i!=-6:
        print(i,end=",")
    elif i==-6:
        print(i,end="\n")
    #b
print("b)",end=" ")
for i in range(-10,21,5):
    if i!=20:
        print(i,end=",")
    elif i==20:
        print(i,end="\n")
    #c
print("c)",end=" ")
for i in range(18,64,9):
    if i!=63:
        print(i,end=",")
    elif i==63:
        print(i,end="\n")
    #d
print("c)",end=" ")
for i in range(18,64,9):
    if i!=63:
        if i%2==0:
            print(i,end=",")
        else:
            print(i*-1,end=",")
    elif i==63:
            print(i*-1,end="\n")"""

"""#task2
car=input("Enter the name of your favorite car ")
c=int(input("Enter a number "))
cn=0
while cn<=c:
    print(car)
    cn+=1 """

"""#task3
sum=0
for i in range(0,601,1):
    if i%7==0 and i%9==0:
        sum+=i
print(sum)"""

"""#task4
sum=0
for i in range(0,601,1):
    if i%7==0 and i%9==0:
        continue
    elif i%9==0:
        sum+=i
    elif i%7==0:
        sum+=i
print(sum)"""

"""#task5
for i in range(10,51,1):
    if i%2!=0:
        print(i,end=" ")"""

"""#task6
sum=0
n=int(input("Enter the number of n: "))
for i in range(1,n+1,1):
    if i%2!=0:
        sum+=(i**2)
    elif i%2==0:
        sum-=(i**2)
print(sum)"""

"""#task7
count=1
sum=0
c=0
while count<=10:
    a=int(input('Number please: '))
    count+=1
    for a in range(a,a+1,1):
        if a%2!=0:
            sum+=a
            c+=1
print("The total of the odd numbers is",sum,"and their average is",sum/c)"""

"""#task8
N=int(input("Enter a number: "))
if N>=7:
    sum=0
    for i in range(0,N+1,7):
        sum+=i
    print(sum)
else:
    print("There is no number")"""

"""#task9
c=0
sum=0
while c<5:
  a=int(input())
  sum+=a
  c+=1
  print(sum)"""

"""#task10
a=int(input("Enter a number "))
while a>0:
    if a%10!=a:
        print(a%10,end=", ")
        a//=10
    else:
        print(a%10,end="")
        a//=10"""

"""#task11
c=0
a=int(input("Enter a number "))
while a>0:
    a//=10
    c+=1
print(c)"""

"""#task12
c=0
a=int(input("Enter a number "))
b=a
while b>0:
    if b//10>=0:
        c+=1
        b//=10
while a>0:
    if a//10!=0:
        print(a//10**(c-1),end=", ")
    else:
        print(a//10**(c-1))
    a%=10**(c-1)
    c-=1"""

"""#taks13
c=0
a=int(input())
for i in range(1,a+1):
    if a%i==0:
        c+=1
        print(i)
    else:
        continue
print(f"Total {c} divisors")"""

"""#task14
sum=0
a=int(input())
for i in range(1,a+1):
    if a%i==0:
        sum+=i
if sum==a:
    print(a,"is a perfect number")
else:
    print(a,"is not a perfect number")"""

"""#task15
div=0
a=int(input())
for i in range(1,a+1):
    if a..%i==0:
        div+=1
if div==2:
    print(a,"is a prime number")
else:
    print(a,"is not a prime number")"""

"""#task16
a=int(input("Quantity = "))
c=0
sum=0
max=0
min=0
while a>c:
    c+=1
    b=int(input("Number please = "))
    sum+=b
    if c==0:
        max=b
        min=b
    elif b>max:
        max=b
    elif b<min:
        min=b
print("Maximum",max)
print("Minimum",min)
print("Average is",sum/a)"""

"""#task17
n=int(input("N = "))
for column in range(n):
    for row in range(1,n+1,1):
        if row==n:
            print("+")
        else:
            print("+",end="")"""

"""#task18
n=int(input("N = "))
m=int(input("M = "))
for column in range(1,n+1):
    for row in range(1,m+1):
        if row==m:
            print(row)
        else:
            print(row,end="")"""

"""#task19
n=int(input("N = "))
for column in range(1,n+1):
    for row in range(1,column+1):
        print(row,end="")
    print()"""

"""#task25
sum=0
b=0
c=1
a=int(input())
print("0 1",end=" ")
for i in range(0,a+1,1):
    if i == c+b:
        print(i,end=" ")
        b=c
        c=i"""
    
"""#task26
a=int(input())
b=""
while a>0:
    b+=str(a%2)
    a=a//2
print(b[-1::-1])"""

"""#task27
a=input()
count=0
b=0
for i in range(-1,-len(a)-1,-1):
    b+=int(a[i])*2**count
    count+=1
print(b)"""

"""#task28
a=int(input())
b=int(input())
for i in range(a,b):
    div=0
    for prime in range(2,i):
        if i%prime==0:
           div+=1
    c=0
    k=""
    if div==0:
        c+=1
        k+=str(c)
        print(i,"is a prime number and the count,",len(k))
"""
"""#task29
a=int(input())
b=int(input())
c=int(input())
for i in range(a,b+1):
    d=str(i)
    x=0
    y=1
    for i in d:
        y*=int(i)
    if y%c==0:
        print(y,end=" ")"""


user1 = int(input(": "))
user2 = int(input(": "))

prime = ""
prime_count = 0
perfect = ""
perfect_count = 0

for i in range(user1, user2+1):
    x = 0
    y = 0
    if i !=0 and i != 1:
        for j in range(1, i):
            if  i % j == 0:
                x+=1
        if x == 1:
            prime_count +=1
            prime+=str(i)+','
    if i!=0:
        for j in range(1, i):
            if i % j == 0 :
                y += j
        if i == y:
            perfect+=str(i)+','
            perfect_count+=1
print(f"""Between {user1} and {user2},
Found {prime_count} prime numbers
Found {perfect_count} perfect numbers
Prime numbers: {prime[:-1]}
perfect number: {perfect[:-1]}""")