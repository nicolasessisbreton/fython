a = {1:1, 2:2}
b = {3:3}

a.update(b)

print(a)
b[3] = 10
print(a)
print(b)