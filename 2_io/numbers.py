def readInput():
    line1 = input()
    line2 = input()
    line3 = input()
    #把字串轉成整數 , 才能做後續的運算
    num1 = int(line1)
    num2 = int(line2)
    num3 = int(line3)

    print(num1+1)
    print(num2+1)
    print(num3+1)

#readInput()
#numbers.py < 1.txt
# 1.txt:
# 10
# 20
# 30

def readInput1():
    line = input()
    cnt = int(line)
    for i in range(0,cnt):
        line = input()
        num = int(line)
        print(num+1)

#numbers.py < num.txt

readInput1()