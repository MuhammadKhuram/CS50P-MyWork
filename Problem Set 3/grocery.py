
grocery = []

while True:
    try:
        grocery.append(input().upper())
    except EOFError:
        break


unique_grocery = set(grocery)
unique_grocery = sorted(unique_grocery)
for item in unique_grocery:
    print(grocery.count(item), item)
