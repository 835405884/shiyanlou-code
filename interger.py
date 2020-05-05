days = int(input("Enter days:"))
months = days // 30
day = days % 30
print("Way1:Months = {},Days = {}".format(months, day))
print("Way2:Months = {},Days = {}".format(*divmod(days,30)))
#divmod(num1,num2) is indictate  return a tuple which have two values
#first is num1//num2,second is num1%num2
#the * is unpack to the tuple
