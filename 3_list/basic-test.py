x = [2,3,4]
# i is element
for i in x:
    print(i,end=" ")
print()

# i is position
# range(len(x)) = range(0,len(x),1)
for i in range(len(x)):
    print(x[i],end=" ")
print()

# idx & value
'''
idx 是編號從0開始
'''

for idx, i in enumerate(x):
    print(idx+1,i,sep=":")
print()

x.append(5)
print(x)

y = [6,7]
z = x+y
print(x,y,z,sep="\n")
print()

z=x
z[0] = 99
print(x,z,sep="\n")
#改變z的同時也會順便改變x的值

'''
z = x 
z跟x指向同一個開始位子
'''

x.append(y)
print(x)
print()

print(len(x))
print(x[-1])
'''
 = print(x[len(x)-1])
最後一個x值
c++無法使用此做法
'''
print()
print(x)
x[2:3] = [90,91,92]
#把index 2和index 3的 index換成90,91,92
#盡量少用
print(x)



