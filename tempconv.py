print ("welcome to temperature converter")
temp = input ('What is the temperature you would like to convert')
sign = temp[-1]
temp = int(temp[:-1])


if sign == "k" or sign =="K":
    temp = round(temp-273.15)
    print(str(temp)+'C')
    
elif sign == "F" or sign =="f":
    temp = round(temp * (100/212))
    print(str(temp) + 'C')