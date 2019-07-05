#!/usr/bin/env python
# coding: utf-8

# In[43]:


# If an even number is multiplied with an odd number then the product of the two numbers is even
# The sum of an even and odd number is odd
# The logic is to pair the even and the odd numbers in a way that the product is even and the sum of these numbers is odd


#Function to match the pairs of numbers in the list whose product is even and sum is odd 

def pair_matcher(integers, n):   #Function with two input arguments
   list_even=[]  #List to store the even numbers
   list_odd=[]   #List to store the odd numbers
   
   #Iterating through the the length of the list of the integers
   for i in range(0, n):
      
       #Checking for even numbers using a modulus operator
       if ((integers[i] % 2) == 0):  # If the number is divided by 2 and remainder is 0 then it is even
           list_even.append(integers[i])  #Using .append function to add the even numbers to an empty list
       
       #If the above condition is not true then it is an odd number
       else:
           list_odd.append(integers[i])  #Using .append function to add the odd numbers to an empty list
           
   print("The pairs of numbers in the list whose product is even and sum is odd are: ") #Using a print statement
   
   list_pairs=[]  #List to store the pairs of integers in the list whose product is even and sum is odd
   
   for x in range(len(list_even)): #Iterating through the list of even integers
       for y in range(len(list_odd)): #Iterating through the list of odd integers
           list_pairs.append((list_even[x],list_odd[y]))  #appending the matched pair of numbers
   print(list_pairs)  #Printing out the matched pair of numbers
   
#Getting the input from the user for the required list of integers
user_input = input("Please enter the required integers seperated by space and hit enter: ") 

user_input_list= (user_input.split())  #Converting the input into a list using .split function with space as a delimitter
integers=[]  #List to store the integers converted as int type

#The given input is in the form of string type and needs to be converted to int type for computation

#Converting the input from string type to integer type
for i in range(len(user_input_list)):  #Iterating through the elements in the list 
   integers.append(int(user_input_list[i]))  #Appending the int type converted elements to a new list "integers"
length_list= len(integers)  #Calculating the length of the list of integers


pair_matcher(integers, length_list) #Invoking function to match the pairs of numbers


# In[ ]:




