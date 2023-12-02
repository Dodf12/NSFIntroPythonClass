def triangle_type(a, b, c):
  if a == b == c:
      return "Equilateral Triangle"
  elif a == b or b == c or a == c:
      return "Isosceles Triangle"
  else:
      return "Scalene Triangle"


side_a = int(input("Enter the length of side A: "))
side_b = int(input("Enter the length of side B: "))
side_c = int(input("Enter the length of side C: "))

result = triangle_type(side_a, side_b, side_c)
print("The triangle is a", result)

def find_season(month, day):
  if (month == 3 and day >= 20) or (month > 3 and month < 6) or (month == 6 and day < 21):
      return "Spring"
  elif (month == 6 and day >= 21) or (month > 6 and month < 9) or (month == 9 and day < 23):
      return "Summer"
  elif (month == 9 and day >= 23) or (month > 9 and month < 12) or (month == 12 and day < 21):
      return "Fall"
  else:
      return "Winter"


month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))

result = find_season(month, day)
print(f"The season for {month}/{day} is {result}.")

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
      print("FizzBuzz")
  elif number % 3 == 0:
      print("Fizz")
  elif number % 5 == 0:
      print("Buzz")
  else:
      print(number)
def fibonacci(n):
  if n <= 0:
      return "Invalid input. Please enter a positive integer."

  fib_sequence = [0, 1]
  while len(fib_sequence) < n:
      fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

  return fib_sequence[n - 1]


n = int(input("Enter the value of n: "))
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")

def analyze_speed(road_type, speed):
  if road_type.lower() == "highway":
      speed_limit = 70
  elif road_type.lower() == "city":
      speed_limit = 30
  else:
      return "Invalid Road Type. Please enter 'highway' or 'city'."

  speed_percentage = (speed / speed_limit) * 100

  if speed_percentage <= 80:
      return "Slow"
  elif speed_percentage <= 100:
      return "Right Speed"
  elif speed_percentage <= 105:
      return "Slightly Fast"
  else:
      return "Very Fast"


road_type = input("Enter the road type (highway or city): ")
car_speed = float(input("Enter the speed of the car: "))

result = analyze_speed(road_type, car_speed)
print(f"The vehicle is going: {result}")
