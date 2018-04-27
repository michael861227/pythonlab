print("Hello word")
print("Hello","world")
print("Hello","world",sep="-")
#sep 內定為字串和字串中間空白建 , 因此可以自己指定

print("Hello","world",sep="&",end="%")
#end 內定為字串結束是換行
print("ABC")

print()
print(9//2)
print(9 % 5)
print(3 ** 4)
# 等同於3的4次方

print()
#變數宣告可以不用寫
a = 1
b = 2
print(a+b)

print()
str1 = "I am learning programing"
print(str1)
print(len(str1))

print(str1[2])
print(str1[5:13]) #從第五的index到第13個index
print(str1[5:])
print(str1[:])
print(str1[::-1]) #字串相反印

print("{0} {1}".format(100,200)) #用形式決定
print("num1: {0} num2: {1}".format(a,b))
print("{0:10} {1:10}".format(200,300)) #決定占10個字元
print("{0:<7}{1:<7}{2:<7}".format(12345,456,78999))#向左對齊占7個字元
print("{0:>7}{1:>7}{2:>7}".format(12345,456,78999))

print()

s = "Stone Campus"
#這個字串的長度
print("字串長度",len(s))
#位置 6 的字母 (使用 [])
print(s[6])
#從位置 3 到 9 的子字串 "ne Camp" (使用 [:])
print(s[3:9])
#從位置 3 到 最後的子字串 "ne Campus" (使用 [:])
print(s[3:])
#從位置 0 到 10 的子字串 "Stone Camp"  (使用 [:])
print(s[:10])