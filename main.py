
num_1 = int(input("Please enter a Number? "))
num_2 = int(input("Please enter another Number? "))
num_3 = int(input("Please enter another Number? "))
num_4 = int(input("Go on, give me one more? "))

calca = (num_1 + num_2)
calcb = (num_2 - num_3)
calcc = (num_3 * num_4)
calcd = (num_1 / num_4)
print ("_____You have 4 options a, b, c or d_____")
print ("a: To add the 1st and 2nd number")
print ("b: To subtract the 3rd number from the 2nd number")
print ("c: To multiply the 3rd and 4th number")
print ("d: To divide the 4th number by the 1st number")
option = input("Please select a letter a, b, c or d? ")

if option == "a":
    print(calca)
elif option == "b":
    print(calcb)
elif option == "c":
    print(calcc)
elif option == "d":
    print(calcd)
else:
  print ("_______________________________")
  print ("Wrong option, please try again.")
  