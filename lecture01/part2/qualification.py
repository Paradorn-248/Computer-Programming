w = float(input('Weight: '))
h = float(input('Height: '))
bmi = w / ((h/100)**2)

if bmi >= 30 :
    print(f"Your BMI is {bmi:.1f} You're in the obese range.")
elif bmi >= 25 :
    print(f"Your BMI is {bmi:.1f} You're in the overweight range.")
elif bmi >= 18.6 :
    print(f"Your BMI is {bmi:.1f} You're in the healthy weight range.")
else :
    print(f"Your BMI is {bmi:.1f} You're in the underweight range.")
