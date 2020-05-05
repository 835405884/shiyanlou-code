x = float(input("Enter the x: "))
n = float(input("Enter the n: "))
i = n
ex = 1
m = n - 1
yuxiang = 0
while x <= 1 and x >= 0 and n >= 1:
    xiang = ((x ** n)/n)
    while  m >= 2:
        xiang = xiang/m
        m = m - 1
    ex = ex + xiang
    n = n - 1
    print("when x={},n={},the result is {}".format(x, i, ex))
while x > 1 or  x < 0 and n == 0:
    print("x is not belong (0,1),cannot calculate!")

