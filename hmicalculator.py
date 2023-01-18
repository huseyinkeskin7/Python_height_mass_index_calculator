import time

print("Written by Hüseyin Berk Keskin")

time.sleep(0.5)
print("Please enter your height and weight respectively!")
height = float(input("Height(please write with point like 1.81) = "))
weight = float(input("Weight = "))
bmi = weight/(height**2)
print("Height Mass Index:",bmi,"kg/m2")
if bmi<18.5:
    print("You are below your ideal weight")
elif 18.5<bmi<24.9:
    print("You are at your ideal weight")
elif 25<bmi<29.9:
    print("You are above your ideal weight")
elif 30<bmi<39.9:
    print("You are far above your ideal weight1")
