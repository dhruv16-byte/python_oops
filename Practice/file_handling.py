with open("practice.txt", "w") as file:
    file.write("1,2,3,4,5,6,7,8,9,10")
count = 0
with open("practice.txt", "r") as file:
    data = file.read()
    for i in data:
        if i == ",":
            pass
        else:
            even = int(i)
            if even % 2 == 0:
                count += 1
    print(count)
