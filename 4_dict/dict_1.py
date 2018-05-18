ages = {}

def prAge(name):
    if(ages.get(name)):
       print(name, ages.get(name))
    else:
        print("N/A")

def test():
    num = int(input())
    print(num)
    for i in range(0,num):
        line = input()
        tokens = line.strip().split()
        #strip 會把line的空白或雜資料去掉
        name = tokens[0]
        age = int(tokens[1])
        ages[name] = age
    print(ages)
    print()
    #print name and age
    num = int(input())
    for i in range(0,num):
        line = input()
        print(line)
        prAge(line)
        print()

test()