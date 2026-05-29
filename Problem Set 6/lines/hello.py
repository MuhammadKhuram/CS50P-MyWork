import sys

if len(sys.argv) < 2:
    print("Too few command-line arguments")
#fjjgm
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
 ###nvnk
elif not sys.argv[1].endswith(".py"):
    print("File does not exist")
   #jnksjvn
else:
    count = 0
    with open(sys.argv[1], "r") as file:
        for line in file:
            if line.lstrip().startswith("#"):
                pass
            else:
                count = count+1

print(count)
