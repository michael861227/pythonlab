num = list(range(5,0,-1))
print("list(range(5,0,-1)):",num)

num[2] = 100
print(num)

a = [1,2,3]
total1 = sum(a)
print(total1)

total2 = sum(list(range(5,0,-1)))
print(total2)

strA = "Stone"
strA = list(strA)
strA[0] = "Y"
#join only apply for string pass
print(''.join(strA))
print(','.join(strA))

