# Creating 2 number variables and asking the user for input
# Creating Calculation function to hold the request for input and calculations 
def calculation(): 
  num_1 = input("Please enter a Number? ")
  # Confirm whether the input is an integer 
  try:
  # Checking whether input is an integer
    num_1 = int(num_1)
  except ValueError:
    print ("Incorrect value.")
    # Calling Run function to confirm whether the user wants to try again as the input is no an integer
    run()   
  num_2 = input("Please enter another Number? ")
  # Confirming whether the input is an integer 
  try:
    num_2 = int(num_2)
  except ValueError:
    print ("Incorrect value.")
    run()
    
# Creating the 4 calculations to make up options a, b, c & d
  calca = (num_1 + num_2)
  calcb = (num_2 - num_1)
  calcc = (num_2 * num_1)
  calcd = (num_2 / num_1)
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
    run()
# Creating a run function to give the user the option to try again  this will either restart the program or say 
def run(): 
  while True:
    runagain = input("Would you like to try again? (Y/N) ")
    if runagain not in ('Y', 'N'):
      print ("Incorrect Answer.")
      run()
      break
    if runagain == 'Y':
        calculation()
        run()
        break
    else:
      print("\n")
      print("Thank you for using the Calculator.")
      break

calculation()
run()
