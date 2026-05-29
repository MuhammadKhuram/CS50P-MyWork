name = input("camelCase: ")

for i in range(len(name)):
    if name[i].isupper():
        name = name.replace(name[i], "_" + name[i].lower())

print(name)
 