#Example 1
'''
List = []
print("Blank List: ")
print(List)

List = [10, 20, 14, 28, 32, 64]
print("\nList of numbers: ")
print(List)

List = ["Monday", "Tuesday","Wednesday","Thursday","Friday", "Saturday","Sunday"]
print("\nList Items: ")
print(List[0])
print(List[1])
print(List[2])
print(List[3])
print(List[4])
print(List[5])
print(List[6])

List = [['Black'], ['Brown'],['Blue']]
print("\nMulti-Dimensional List: ")
print(List)
'''




#Example 2
'''
List = []
print("Initial blank List: ")
print(List)

List.append(0)
List.append(1)
List.append(2)
print("\nList after Addition of Three elements: ")
print(List)

for i in range(3, 7):
 List.append(i)
print("\nList after Addition of elements from 3-6: ")
print(List)

List.append((9, 13))
print("\nList after Addition of a Tuple: ")

print(List)

List2 = ['are', 'Real Numbers']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)
'''



#Lab Activity 1
'''
List1=[]
print('Enter elements of First List: ')
for i in range(5):
    v=input('Enter a value : ')
    n=int(v)
    List1.append(n)

List2=[]
print('Enter elements of Second List: ')
for i in range(5):
    v=input('Enter a value : ')
    n=int(v)
    List2.append(n)

List3=List1+List2
print(List3)
'''


#Lab Activity 2
'''
word=input('Enter Word to Check: ')
def isPalindrome(word):
    temp=word[::-1]
    if temp.capitalize()==word.capitalize():
        return True
    else:
        return False

print(isPalindrome(word))
'''


#Lab Activity 3
'''
a=[[1,0,0],[0,1,0],[0,0,1]]
b=[[1,2,3],[4,5,6],[7,8,9]]
c=[]
for row in range(3):
   c.append([])
   for colmn in range(3):
       c[row].append(0)
       for aux in range(3):
           c[row][colmn] += a[row][aux] * b[colmn][aux]

print(c)
'''



#Lab Activity 4
'''
def perimeter(lis):
    leng=len(lis)
    perimeter=0;
    for i in range(0,leng-1):
        dist = (((lis[i][0]-lis[i+1][0])**2)+((lis[i][1]-lis[i+1][1])**2))**0.5
        perimeter= perimeter + dist
    perimeter= perimeter + (((lis[0][0]-lis[leng-1][0])**2) + ((lis[0][1]-lis[leng-1][1])**2))**0.5
    return perimeter
L= [(1,3),(2,7),(3,9),(-1,8)]
print(perimeter(L))
'''



#Lab Activity 5
'''
def symmdiff(a,b):
    e=set()
    for i in a:
        if i not in b:
            e.add(i)
    for i in b:
        if i not in a:
            e.add(i)
    return e

set1={0,1,2,3,4}
set2={4,5,6,7,8,9}
print(symmdiff(set1,set2))

print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))
print(set1^set2)
print(set2^set1)
'''


#Lab Activty 6
'''
eg={('Shoaib','Ali'):'02303213433',('aib','li'):'02342421421',('sib','ai'):'021321434532',}
firstName=input('Enter First Name: ')
lastName=input('Enter Last Name: ')

searchTuple = (firstName, lastName)
if searchTuple in eg:
    print(eg[searchTuple])
else:
    print('Name Not Found')
'''

#Lab Task 1
'''
a=[]
c=[]
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    a.append(b)
n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    c.append(d)
new=a+c
new.sort()
print("Sorted list is:",new)
'''

#Lab Task 2
'''
a=[]
c=[]
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    a.append(b)
n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    c.append(d)
new=a+c
n=n1+n2
new.sort()
print("Sorted list is:",new)
print("Largest element is:",new[n-1])
print("Smallest element is:", new[0])
'''

#Lab Task 3


#Lab Task 4
'''
if __name__ == '__main__':

    birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'}

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)

    print('Who\'s birthday do you want to look up?')
    name = input()
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))
'''


#Lab Task 5
'''
Dictionary = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]

newDictionary = {k: Dictionary[k] for k in keys}
print(newDictionary)
'''

