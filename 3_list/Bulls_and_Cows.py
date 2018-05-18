def result(answer,guess):
    A=0
    B=0
    for idx_ans , val_ans in enumerate(answer):
        if answer[idx_ans] == guess[idx_ans]:
            A += 1
        else:
            for idx_gue,val_gue in enumerate(guess):
                if val_ans == val_gue and idx_ans != idx_gue:
                    B += 1
    return str(A)+"A"+str(B)+"B"

print(result("1234",'4321'))
print(result('4657','9658'))
print(result('9876','6879'))