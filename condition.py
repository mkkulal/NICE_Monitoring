from unittest import result


raining = input("Is is raining? (yes/no) :" )
if raining == "yes" :
    print ("You need an umbrella")

num = input ("Enter a number : ")
n = int (num)
if num < 5 :
    print ("Input is less than 5")

def minimum(x,y):
    if x < y:
        return x
    else:
        return y

result = minimum(2.2,5)
print (result)


raining = input("Is is raining? (yes/no) :" )
umbrella = input("Do you have umbrella? (yes/no) :" )
if raining == "yes" and umbrella == "yes":
    print ("Don't forget your Umbrella when you step out")
elif raining == "yes" and umbrella == "no":
    print ("wear a Jacket")

x = input("Enter number:")
x = float(x)
if x < 2:
    print ("THe nuber less than 2")
elif x < 6:
    print ("THe nuber less than 6")
elif x < 8:
    print ("THe nuber less than 8")

def abs_val(num):
    if num < 0:
        return -num
    elif num == 0:
        return num
    else:
        return num
result = abs_val(7.84)
print (result)

