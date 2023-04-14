print("Enter the length in centimeter::")

c, m, k = float(input()), 0, 0
# c = centimeter
# m = meter
# k = kilometer

# It will convert the centimeter into meter and kilometer values
m = (float)(c / 100)
k = (float)(c / 100000)

# It will print the final output
print("Length in Meter      = ", m, " meter")
print("Length in Kilometer  = ", k, " kilometer")