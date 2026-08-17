with open("file1.txt", "r") as f1, \
     open("file2.txt", "r") as f2, \
     open("file3.txt", "r") as f3, \
     open("result.txt", "w") as out:

    a = f1.readlines()
    b = f2.readlines()
    c = f3.readlines()

    for i in range(len(a)):
        x = a[i].strip()
        y = b[i].strip()
        z = c[i].strip()

        out.write(f"|{x:<20}|{y:<20}|{z:<20}|\n")