#create a set from a string with the set function
a = 'abracadabra'
a_set = set(a)

#create a set from a list with the set function
b = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]
b_set = set(b)

#iterate over a_set
for c in a_set:
    print(c, end = ' ')

print('')

#iterate over b_set
for n in b_set:
    print(n, end = ' ')

print('')

#add to a_set
a_set.add('c')
print(a_set)

#remove from b_set
b_set.remove(10)
print(b_set)
