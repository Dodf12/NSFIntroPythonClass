#1
print("Welcome! please enter your time in 24 hour clock format!" )
hours = input("Please enter the number of hours passed: ")
minutes = input("Please enter the number of minutes passed: ")
if int(hours) > 12:
  hours = int(hours) % 12


if int(minutes) > 59:
  minutes = int(minutes) % 60
  hours = int(hours) + 1

print(str(hours) + ":" + str(minutes))

#2
minutesr = int(input("Enter minutes: "))
hours = minutesr // 60
minutes = minutesr % 60
print(f"{minutesr} minutes is {hours} hours and {minutes} minutes")
#3
miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the number of gallons used: "))
mileage = miles_driven / gallons_used
print("The mileage of the car is: ", mileage)













