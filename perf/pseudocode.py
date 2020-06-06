MAX=10
a = list(range(1, MAX))
print(a)
print(a[1:3])
l = len(a)
p = ((l / 2) - 2)
q = ((l / 2) + 2)
print(a[int(p):int(q)])
print(a[-4:])
i = 0
j = 0
for i in range(1, MAX):
    print("---------Outer loop----------------")
    print("i = ", i)
    for j in range(1, min(10, i)):
        print("j = ", j)
    print("after inner for loop i is:", i)
    print("after inner for loop j is:", j)
    k1 = int(i / 5)
    print("k1 = ", k1)
    k2 = int((2 * i)/5)
    print("k2 = ", k2)
    k3 = int((3 * i)/5)
    print("k3 = ", k3)
    k4 = int((4 * i)/5)
    print("k4 = ", k4)
    a1= max(i-10, 0)
    a2= i
    for x in range(a1, a2):
        print("x = ", x)
