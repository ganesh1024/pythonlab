n = int(input('Enter the size of list'))
list=[]
print('enter the elements in List')
for i in range(n):
    element=int(input());
    list.append(element)

print(list)

print('Sorted List:')
list.sort()
print(list)

print('List in Reverse order:')
list.reverse()
print(list)

print('The last element of list is',list[-1])

for i in list:
    print(i)

list.insert(1,8)
print("Number inserted at index 1 is:",list[1])
print(list)

list.remove(44)
print(list)
print('max element is :', max(list))
print('min element is :', min(list))

print("the poped element is:",list.pop(0))

list.clear()
print(list)
