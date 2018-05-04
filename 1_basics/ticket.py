def ticket1(age):
    if age <15:
        print("children")
    elif age <65:
        print("adults")
    else :
        print("seniors")

def test():
    ticket1(10)
    ticket1(20)
    ticket1(65)
    print()
    ticket2(10)
    ticket2(20)
    ticket2(65)
    print()
    ticket3(10)
    ticket3(20)
    ticket3(65)

def ticket2(age):
    if age < 15: print("children")
    elif age < 65 : print("adults")
    else: print("seniors")

def ticket3(age):
    tickettype = "children" if age <15 else "adults" if age<65 else "seniors" 
    print(tickettype)

test()
