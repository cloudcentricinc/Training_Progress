#parrot = "narrow blue"

#print(parrot)
#print(parrot[10])
#print(parrot[8])
#print(parrot[5])
#print(parrot[6])
#print(parrot[7])
#print()
#print(parrot[-1])
#print(parrot[-10])
#print()
#print(parrot[2-11])
#print(parrot[0:6])
#print(parrot[3:6])
#print(parrot[0:9])
#print(parrot[:9])
#print(parrot[6:])
#print(parrot[:6] + parrot[6:])
#print(parrot[:])
#print(parrot[-4:2])
#print(parrot[-4:10])
#print(parrot[-8:-9])

#print(parrot[0:6:8])
#print(parrot[0:6:3])
number = input("please enter a series of number,using any separators you like")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char
#print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
