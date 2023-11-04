#problem1

celsius = float(input("enter temperature in celsius:"))
fahrenheit = (celsius * 9/5) + 32
print("\nTemperature in fahrenheit:",fahrenheit)

#problem2

area = 346.5
radius = 0.0
pi = 3.14
radius = area / pi
radius = radius ** 0.5
print(radius)
print(2*pi*radius)

#problem3

T=0
V=0

Wind_Chill =  35.7 + (0.6 * T) - (35.75 * (V ** 0.16)) + (0.43 * T * (V ** 0.16))
print(Wind_Chill)
