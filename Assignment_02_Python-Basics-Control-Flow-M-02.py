"""
Assignment_02_Python-Basics-Control-Flow-M-02
Assignment-02 Questions:

##
Question 1: Loop Basics (for loop)
Write a Python program that uses a for loop to print numbers from 1 to 10.

##
Question 2: Loop with Condition
Using a for loop, print only the even numbers between 1 and 20.


##
Question 3: String Manipulation
Take a string input from the user and:
1. Print the string in uppercase
2. Print the length of the string
3. Print the string reversed

##
Question 4: String Processing with Loop
Take a string from the user and count how many vowels (a, e, i, o, u) are in the string.

##
Question 5: List Comprehension
Given the list:
numbers = [10, 25, 30, 45, 50, 65, 70]
Using list comprehension:
1. Create a new list containing only numbers greater than 40
2. Print the new list
"""


#Question 1: Loop Basics (for loop)
for i in range(1,11):
  print(i) #1,2,.....,9,10.

#Question 2: Loop with Condition
for i in range(2,21): #loop start
  if i % 2 == 0:  #Condition
    print(i) #2,4,6,8,.....,18,20.

#Question 3: String Manipulation
text = input("Enter a string: ") #input take from user (shehab)
print(f"inputed string: {text}") #print the taken input

#string in uppercase
print(text.upper()) #SHEHAB

#length of the string
print(len(text)) #6

#string reversed
text = text[::-1]
print(text) #bahehs


#Question 4: String Processing with Loop
text = input("Enter a string: ") #input string from user (shehab)
count = 0 #initially count value 0
vowel = "aeiouAEIOU"

for i in text: #start for loop
  if i in vowel: #condition
    count = count + 1 
print("Total number of vowels:",count) #show total number of vowel output (=2)


#Question 5: List Comprehension
numbers = [10, 25, 30, 45, 50, 65, 70] #given list
new_numbers = [] #take empty list

for i in numbers:
    if i > 40:
        new_numbers.append(i)

#print the new list
print(new_numbers) #[45, 50, 65, 70]


#Alterntive way
numbers = [10, 25, 30, 45, 50, 65, 70]

# 1. Create a new list containing only numbers greater than 40
new_numbers = [i for i in numbers if i > 40]

# 2. Print the new list
print(new_numbers)



