# num = float(input("input float number: "))
# decimal_val = ("{:.2f}".format(num))
# print (decimal_val)

# #solution metod 2
# num = float(input("input float number: "))
# print (f"{num:.2f}")

#solution metod 3
num = float(input("input float number: "))
float_two = int(num*100)%100/100+int(num)
print(float_two)