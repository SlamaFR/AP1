i = 145
count = 0
while i <= 256:
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        count += 1
        print(i)
    i += 1

print(count, "entiers")
