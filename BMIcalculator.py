age = float(input("Enter your age: "))
sex = input("Enter your Sex , if Male type 'male' or if Female type 'female'  : ")
height = float(input("Enter your Height in meters: "))
weight = float(input("Enter your Weight in kilograms: "))
bmi = (weight/(height**2))

if(age>=20):
    if(bmi<16):
        print("You have Severe Thinness. "+ str(bmi) +" is your BMI . Please seek help of a doctor ")
    if(bmi>=16 and bmi<=17):
        print("You have Moderate Thinness. "+ str(bmi) +" is your BMI . Visit a doctor regarding your BMI. ")
    if(bmi>17 and bmi<=18.5):
        print("You have Mild Thinness. "+ str(bmi) +" is your BMI . Eat healthy food and Excercise daily . ")
    if(bmi>18.5 and bmi<=25):
        print("You have Normal Weight . "+ str(bmi) +" is your BMI . Eat healthy food and Excercise daily . ")
    if(bmi>25 and bmi<=30):
        print("You are Overweight. "+ str(bmi) +" is your BMI . Visit a doctor regarding your BMI. ")
    if(bmi>30 and bmi<=35):
        print("You are Obese Class I . "+ str(bmi) +" is your BMI . Please seek help of a doctor. ")
    if(bmi>35 and bmi<=40):
        print("You are Obese Class II . "+ str(bmi) +" is your BMI . Please seek help of a doctor. ")
    if(bmi>40):
        print("You are Obese Class III . "+ str(bmi) +" is your BMI . Please seek Emergency help of a doctor. ")
        
if(age<20 ):
    print("Your BMI is "+ str(bmi) +". Visit a doctor for regarding your BMI for proper knowledge and checkup . ")
    
    
    
    
    
        
    
        

