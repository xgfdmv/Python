max = None
min = None

while True:
    num = input("Enter a number: ")

    if num =='done':
        break
    try:
        num == float(num)
    except:
        print("Invalid input!")
        continue

    if max is None:
        max = num
        min = num
    elif max < num:
        max = num
    elif min > num:
        min = num

print("max is: ",max)
print("min is: ",min )
