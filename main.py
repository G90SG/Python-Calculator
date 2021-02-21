# Creating 4 number variables and asking the user for input 
num_1 = int(input("Please enter a Number? "))
num_2 = int(input("Please enter another Number? "))
num_3 = int(input("Please enter another Number? "))
num_4 = int(input("Go on, give me one more? "))

# Creating the 4 calculations to make up options a, b, c & d
calca = (num_1 + num_2)
calcb = (num_2 - num_3)
calcc = (num_3 * num_4)
calcd = (num_1 / num_4)
# Printing a line space
print("\n")

# Print instructions to the user and ask for a choice of a, b, c or d
print ("_____You have 4 options a, b, c or d_____")
print ("a: To add the 1st and 2nd number.")
print ("b: To subtract the 3rd number from the 2nd number.")
print ("c: To multiply the 3rd and 4th number.")
print ("d: To divide the 4th number by the 1st number.")
option = input("Please select a letter a, b, c or d? ")
# Printing a line space
print("\n")

# Creating an IF statement to print a string including the anser to the chosen calculation 
if option == "a":
    print("You selected 'a', which adds the 1st and 2nd number which equals" , calca,".")
elif option == "b":
    print("You selected 'b', which subtracts the 3rd number from the 2nd which equals", calcb,".")
elif option == "c":
    print("You selected 'c', which multiplies the 3rd and 4th number which equals", calcc,".")
elif option == "d":
    print("You selected 'd', which divides the 4th number by the first which equals", calcd,".")
else:
# Else if the user enters a letter which is not one of the options, the program will ask the user to try again
  print ("_______________________________")
  print ("Wrong option, please try again.")
