

# if index is last one,println() , otherwise , ","
def prList(arr):
    for idx , i in enumerate(arr):
        if(idx != len(arr)-1):
            print(i,end=",")
        else:
            print(i)

a = [10,20,30,40,50]
prList(a)

b = [30,4,56]
prList(b)

c = ["apple","orange","banana"]

def enumList(arr):
    for idx,i in enumerate(arr):
        #print(idx+1,i,sep=". ")
        print("{}. {}".format(idx+1,i))

enumList(c)