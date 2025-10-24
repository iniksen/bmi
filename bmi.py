w= float(input("enter your weight (kg):"))

h= float(input("enter your height(meter):"))

bmi=w/(h*h)
print (bmi)
print ("your bmi is:",bmi)

if bmi<18.5 :
    print("underweight")
    
elif 18.5<= bmi<=24.9:
    print("normal weight")
    
elif 25<=bmi<=29.9:
    print("overweight")
    
elif bmi>=30:
    print("obesity")
    
else:
     print("invalid BMI value")
    