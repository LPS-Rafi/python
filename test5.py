"""
#task1
b=[]
for i in range(5):
  a=int(input())
  b.append(a)
  print(b)"""

'''#task2
a=input()
b=[]
a=list(a.split(","))
if len(a)>=4:
  for i in a[2:len(a)-2:]:
    b.append(int(i))
  print(b)
else:
  print("Not Possible")'''

'''#task3
li=[]
for i in range(5):
  a=int(input())
  li.append(a)
print("printing values from the list in reverse order:")
for i in li[-1:-len(li)-1:-1]:
  print(i)'''

''''#task4
a=[1,2,3,4,5,6,7]
b=[]
for i in a[::]:
    b.append(i**2)
print(b)'''

'''#task5
a=["hey","there","","what's","","up","","?"]
b=[]
for i in a:
    if i!="":
        b.append(i)
print("Original List:",a)
print("Modified List:",b)'''

"""#task6
a=input()
list=(a.split(","))
list=[int(cha) for cha in list]
print("My list:",list)
max=list[0]
for i in list:
  if i>max:
    max=i
for j in range(len(list)):
  if list[j]==max:
    break
print("Largest number in the list is",max,"which was found at index",j)
"""
'''#task7
list_one=[1,4,7,5]
list_two=[6,1,3,9]
new_list=[]
for i in list_one[:len(list_one)-1:]:
    new_list.append(i)
print(new_list+list_two)'''

'''#task8
list_one=[1,2,3,4,5,6,7,8,9]
list_two=[10,11,12,-13,-14,-15,-16]
l3=[]
for i in list_one:
  if i%2==0:
    l3.append(i)
for j in list_two:
  if j%2==0:
    l3.append(j)
print(l3)'''

'''#task9
a=input()
l1=[]
b=""
l2=[]
for i in a:
  if i==" ":
    l1.append(int(b))
    b=""
  else:
    b+=i
l1.append(int(b))
print("Original list:",l1)
for j in l1:
  if j%2!=0:
    l2.append(j)
print("Modified list:",l2)'''

'''#TASK10
a=input()
list=(a.split(","))
list=[int(cha) for cha in list]
print("Input list:",list)
l2=[]
j=list[0]
for i in list:
    if i!=j:
      l2.append(j)
      j=i
    else:
      j=i
      continue
print("Modified list:",l2)'''

'''#task11
l1=[1,4,3,2,6]
l2=[5,6,9,8,7]
fact= False
for i in l1:
  for j in l2:
      if i==j:
        fact = True
print(fact)'''

'''#task16
a=input()
list=(a.split(","))
list=[int(cha) for cha in list]
print(list)
max=list[0]
max2=list[0]
for i in list:
  if i>max:
    max=i
for i in list:
    if i==max:
      pass
    elif max2<max and max2<i:
      max2=i
for j in range(len(list)):
  if list[j]==max2:
    break
print("2nd Large number",max2,"index",j)'''

'''#task17
a=input()
list=(a.split(","))
list=[int(cha) for cha in list]
print(list)
max=list[0]
min=list[0]
for i in list:
    if i>max:
        max=i
    elif i<min:
        min=i
for j in range(len(list)):
  if list[j]==max:
    break
for k in range(len(list)):
  if list[k]==min:
    break
print(f'Small {min} index {k}')
print(f'Small {max} index {j}')'''

'''#task18
a=input()
l1=list((a.split(", ")))
a=input()
l2=list((a.split(", ")))
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)'''

'''#task19
l1=[1,2,2,4,5,5,7,99,200,303,70]
l2=[1,1,2,3,3,3,4,5,200,500,-5]
list=l1+l2
list=[int(cha) for cha in list]
list.sort()
l3=[]
j=list[0]
for i in list:
    if i!=j:
      l3.append(j)
      j=i
    else:
      j=i
      continue
print(l3)'''

#task20
