#F transform to T
fahrenheit = 0
print("Fahrenheit Celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8
    print("{:5d} {:7.2f}".format(fahrenheit , celsius))
    fahrenheit = fahrenheit + 25
#{:5d} is indictate the int number with width equal to  5 bit
#{:7.2f} is indictate the float number with width equal to 7 bit and remain 2 bit number behind the point.
