#problem1

print("welcome,please enter your time to convert into 12-Hour format")
hours = input( "please enter the hours: ")
minutes = input("please enter the minutes: ")
Time = hours+(":") +minutes
Time2 = str(int(hours) - 12) + ":" + minutes
print(Time2)

#problem2a
def convert_duration():
    minutes = int(input("Enter the time duration in minutes: "))
    
    hours = minutes // 60
    remaining_minutes = minutes % 60
    
    print(f"{minutes} minutes is equal to {hours} hours and {remaining_minutes} minutes.")

convert_duration()
#problem2b
def convert_to_minutes():
    
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    
    total_minutes = hours * 60 + minutes

    print(f"{hours} hours and {minutes} minutes is equal to {total_minutes} minutes.")
convert_to_minutes()

#problem3
def calculate_mileage():
  miles_driven = float(input("Enter the number of miles driven: "))
  gallons_used = float(input("Enter the number of gallons used: "))
  mileage = miles_driven / gallons_used
  print(f"The mileage is {mileage:.2f} miles per gallon.")
calculate_mileage()



#problem4
def calculate_change(amount):
   num_2_dollar_bills = amount // 2
   num_1_dollar_bills = (amount % 2) // 1
   return num_2_dollar_bills, num_1_dollar_bills
amount = float(input("Enter the amount: "))
num_2_dollar_bills, num_1_dollar_bills = calculate_change(amount)
print(f"Change for ${amount:.2f}:")
print(f"{num_2_dollar_bills} 2-dollar bills")
print(f"{num_1_dollar_bills} 1-dollar bills")
