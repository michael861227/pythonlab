import sys

birthdays={}

def test():
    for line in sys.stdin:
        line = line.strip()
        tokens = line.split()

        m = int(tokens[1])
        if(birthdays.get(m):
            birthdays[m] += 1
        else :
            birthdays[m] = 1
        #print(birthdays)

    for i in range(1,13):
        print(i,birthdays.get(i))
test()