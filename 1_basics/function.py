def bmi(kg, m):
  return kg / (m * m)
def check(kg, m=2, name="guest"): #kg沒有預設值 , 因此在使用函數的時候必須給值
  b = bmi(kg, m)
  print(name, 'BMI', b)

check(60, 2, name="bob")  # bob BMI 15.0
check(60, 1.5)              # guest BMI 15.0
check(60)                 # guest BMI 15.0
#check()                   # Error: missing 1 required positional argument: 'kg'