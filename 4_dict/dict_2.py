students={}


def test():
    num = int(input())
    for i in range (0,num):
        line = input()
        tokens = line.strip().split()
        '''
        students[tokens[0]+"-1"] = int(tokens[1])
        students[tokens[0]+"-2"] = int(tokens[2])
        students[tokens[0]+"-3"] = int(tokens[3])    
        students[tokens[0]+"-4"] = int(tokens[4])
        '''
        for j in range (1,5):
            students[tokens[0]+"-"+str(j)] = int(tokens[j])
      
    num = int(input())
    for i in range(0,num):
        line = input()
        if(line):
            print(line,students.get(line))
test()