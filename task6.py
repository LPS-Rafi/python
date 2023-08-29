"""
#task1
a = ("The Institute", ("Best Mystery & Thriller", "The Silent Patient", 68821), 75717,
[1, 2, 3, 400, 5, 6, 7], ("Best Fiction", "The Testaments", 98291))

print(a[3][3])"""

'''
#task2
a=(10, 20, 24, 25, 26, 35, 70)
print(a[2:len(a)-2:])
'''

'''#task3
book_info = (
("Best Mystery & Thriller","The Silent Patient",68,821),
("Best Horror","The Institute",75,717),
("Best History & Biography","The five",31,783 ),
("Best Fiction","The Testaments",98,291)
)
print("Size of the tuple is:",len(book_info))
for i in book_info:
  print(i)'''

'''#task4
book_info = (
("Best Mystery & Thriller","The Silent Patient",68821),
("Best Horror","The Institute",75717),
("Best History & Biography","The five",31783 ),
("Best Fiction","The Testaments",98291)
)
for j in book_info:
  for k in j:
    award,book,vote=j
  print(f"{book} won the '{award}' category with {vote} votes")'''

'''#task5
given = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
a=int(input())
c=0
for i in given:
  if a==i:
    c+=1
print(f'{a} appears {c} times in tuple')'''

'''#task6
given = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
l=[]
for i in given:
  l.append(i)
l2=[]
for i in range(-1,-len(l)-1,-1):
  l2.append(given[i])
print(tuple(l2))'''

"""#task7
given1={'Harry':15, 'Draco':8, 'Nevil':19}
given2={'Ginie':18, 'Luna': 14}
marks={}
for key, value in given1.items():
  marks[key]=value
for key, value in given2.items():
  marks[key]=value
print(marks)"""

'''#task8
a = input()
b = a.split(', ')
d = {}
total= 0
count = 0
for pair in b:
  key, value = pair.split(':')
  d[key] = int(value)
  total += int(value)
  count += 1
if count == 0:
  average = 0
else:
  average = total / count
print(f"Average is {average}.")'''


'''#task9
exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
new={}
a=int(input())
for key,value in exam_marks.items():
  if value>=a:
    new[key]=value
print(new)'''

'''#task10
a={'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}
max=None
maxid=None
for i in a:
  if max==None:
    max=a[i]
    maxid=i
    break
for i in a:
  if a[i]>max:
    max=a[i]
    maxid=i
print(f"The highest selling book fenre is '{maxid}' and the number of books sold are {max}")'''

'''#task11
a = input("String: ")
a = a.lower()
b = {}
for i in a:
  if 'a' <= i <= 'z':
    if i in b:
      b[i] += 1
    else:
      b[i] = 1
print(b)'''


'''#task12
dict_1 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
c=0
for i in dict_1.values():
  for j in i:
    c+=1
print(c)'''

'''#task13
list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
b = {}
for key, value in list_1:
  if key in b:
    b[key].append(value)
  else:
    b[key] = [value]
print(b)'''

'''#task15
a=[(2, 3), (4, 5), (6, 7), (2, 8)]
d=[]
for b,c in a:
  d.append(b*c)
print(d) '''

'''#task16
a_tuple = ( [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])
a=input()
for i in a_tuple:
  i.pop()
  i.append(a)
print(a_tuple)'''

'''#task17
my_dictionary = {'c1':'Red', 'c2':'Green', 'c3':None, 'd4':'Blue', 'a5':None}
b=my_dictionary.copy()
for i,j in b.items():
  if j==None:
    my_dictionary.pop(i)
print(my_dictionary)'''

'''#task18
dict_1 = {'a' : 6, 'b' : 7, 'c' : 9, 'd' : 8, 'e' : 11, 'f' : 12, 'g' : 13}
a=int(input())
x={}
b=int(input())
for key,value in dict_1.items():
  if a<=value<b:
    x[key]=value
print(x)'''

'''#task19
h=[(20, 80), (31, 80), (1, 22), (88, 11), (27, 11)]
a={}
for i in h:
  k=i[1]
  if k in a:
    a[k].append(i)
  else:
    a[k]=[i]
print(a)'''       

#task20

