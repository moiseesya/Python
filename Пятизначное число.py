num = input()
units = int(num[-1])
doz = int(num[-2])
hundreds = int(num[-3])
thousands = int(num[-4])
doz_of_thous = int(num[-5])
print((doz ** units) * hundreds / (doz_of_thous - thousands))
