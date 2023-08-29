"""#task1
a=input()
b=a[::-1]
print(b)"""

"""#task2
a=input()
b=int(input())
s1=""
if len(a)>1:
    for i in a[b::-1]:
        s1+=i
    if len(a)>b:
        for i in a[b+1:len(a):1]:
            s1+=i
print(s1)"""

"""#task3
a=input()
c=0
for i in a:
    if i=="0" or i=="1":
        c+=1
if c==len(a):
    print("Binary Number")
else:
    print("Not a Binary Number")"""

"""#task4
a=input()
if len(a)>3:
    if a[-1:-4:-1]=="tse":
        print(a)
    elif a[-1:-3:-1]=="re":
        b=a[0:len(a)-2:1]+"est"
        print(b)
    else:
        print(a+"er")
else:
    print(a)

#task5
b=""
a= input()
for i in a[:len(a):]:
  b+=i
  print(b)

#task6
a=input()
for i in a[:len(a):]:
  print(i,":",ord(i))

#task7
a=input()
for i in a[:len(a):]:
  b=ord(i)
  c=b+1
  print(chr(c),end="")

#task8
a=input()
for i in a[1:len(a):2]:
  b=ord(i)
  c=b-32
  print(chr(c),end="")"""

"""#task9
a=input()
b=len(a)
v=""
i=0
while i < b-1:
   if a[i]!=a[i+1]:
      v+=a[i]
   i+=1
v+=a[len(a)-1]
print(v)

#ALT

a=input()
b=len(a)
v=""
for i in range(len(a)):
   if a[i]!=a[i-1]:
      v+=a[i]
print(v)"""

"""#task10
a=input()
co=0
for i in range(len(a)):
   if a[i]==",":
      co=i
      break
s1=a[:co]
s2=a[co+2:]
len1=len(s1)
len2=len(s2)
s3=""
if len1>len2:
   for i in range(len2):
      s3=s3+s1[i]+s2[i]
   print(s3+s1[len2:])
if len2>len1:
   for i in range(len1):
      s3=s3+s1[i]+s2[i]
   print(s3+s2[len1:])"""

a=input()
for i in a:
    if 65<=ord(i)<=90 or 97<=ord(i)<=122:
        if int(i)%2==0:
            b=ord(i)+32
        else:
            b=ord(i)    