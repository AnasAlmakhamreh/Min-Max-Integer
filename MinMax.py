
#A function that returns the smallest number(Integer) in a list
def S_number(x):
    Smallest = x[0] #starts with the first number in the list
    a = 1
    for a in range(len(x)):  #Sets the length of the list as the range
        if x[a] < Smallest : #Uses the first number of the list as the refrences to check the second number.
            Smallest = x[a]  
    return Smallest



#A function that returns the Largest number(Integer) in a list works the same way as the other function
def B_number(x):
    largest = x[0]
    b = 1
    for b in range(len(x)):
        if x[b] > largest:
            largest = x[b]
    return largest


x = [15, 23, 1, 5, 8, 8, 6, 4, 8, 3, 5, 56, -5, 12, 10, 10]
  

#Saving the returned values.    
Large = B_number(x)
Small = S_number(x)

#Printing the returned values
print(Small)
print(Large)













