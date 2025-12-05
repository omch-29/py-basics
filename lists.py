#Lists are mutable

list = [1,6,2,5]
print(len(list))
# for i in list:print(i)
list.append(10)
list.insert(0,0)
list.sort()
list[1]=4
list.sort()
for i in list:print(i)