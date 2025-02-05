name="Kareem Sayed"
first_space=name.index(' ')
firstName=name[:first_space]
secondName=name[first_space:]
print("firstName: "+ firstName)
print("secondName: "+ secondName)


lst = [1,2,3,4,5]
if not lst:
    print("none")
else:
    lst.pop()
    print(lst)
