

#Kristin Goselin

# Each of the sentences below are followed by a set of related instructions.
# After each instruction, add your code that does what's being asked, as well as
# a print statement that shows your work. Don't forget to print new lines as well,
# or your output will be a mess!

import re

solution_separator = "\n\n****************************************\n\n"

# For example:
s0 = "This is a test"
print(s0 + "\n")

print(solution_separator)

# 1) Write a regular expression and if statement that checks if T is the first letter
pattern = "T"
if re.search(pattern, s0):
   print("It starts with 'T'!" + "\n")
else:
   print("My regex is incorrect, it should detect the 'T'!" + "\n")

print(solution_separator)

# 2) Use a regular expression to decompose the string into words and place those words into a list.
#    Extract the first word into a variable and print it
pattern = " "
words = re.split(pattern, s0)
print(words)
print("\n")
first_word = words[0]
print("The first word is: '" + first_word + "'\n")

print(solution_separator)

# 3) Split the sentence into an array of individual words called words and use a for loop to print it.
#    for each var in vars:
#        (your code here)
#
pattern = " "
words = re.split(pattern, s0)
for word in words:
    print(word + "\n")


print(solution_separator)


# 4)
s1 = "Mary was born on September 17, 1986"

# a) Write a regular expression and if statement that checks if the name "Mary" in the sentence.
# b) Write a regular expression and if statement that checks if the sentence contains a 4 digit number.
# c) Write a regular expression to extract that number into a variable b_year and print it in this sentence:
#    "The person was born in b_year."
pattern = "Mary"
if re.search(pattern, s1):
   print("'Mary' is in the sentence.")
else:
   print("My regex is incorrect, it should detect the 'Mary'!" + "\n")
pattern = r'\d\d\d\d'
if re.search(pattern, s1):
   print("There is a four digit number in the sentence")

else:
   print("My regex is incorrect, it should detect the four digit number!" + "\n")




print(solution_separator)

# 5)
s2 = "The dog, named Dog, was doggedly trying to dodge the fog."

# a) Write a regular expression to match the word "dog", but not the name "Dog"
# b) Save the output from this match into a list and print the list to verify it is not matching anything else.
# c) Write a regular expression to match "dog" and "Dog" using a flag (see the cheat sheet).
# d) Write a regular expression to match "dog" or "fog"
# e) Print all outputs.

dog = re.findall("dog", s2)
print(dog)
Dog = re.findall("dog", s2, re.IGNORECASE)
print(Dog)
og = re.findall("[^D]og", s2)
print(og)



print(solution_separator)


# 6)
s3 = "18785 is the 5 digit number I want not 43744, 34553, or 11111"

match = re.search(r'\d\d\d\d\d', s3)
print(match.group())
pattern = r'\d\d\d\d\d'
numbers = re.findall(pattern, s3)
print(numbers)

# a) Write a regular expression to extract the first number (try to do it without using the exact string).
# b) Write a regular expression to extract all numbers, store them in an array, then print the array.

print (solution_separator)

# 7) Write a regular expression to trim the left and right whitespace and print the trimmed output.
s4 = "    There is preceding white space in this sentence, and whitespace at the end        "
pattern = re.compile(r'\s+')
s4 = re.sub(pattern, '', s4)
print(s4)

print (solution_separator)

# 8)
s6 = "The date 5/17/1982 is trickier to get"
F_date = re.findall(r"\d.\d\d.\d\d\d\d", s6)
print(F_date)
month = [i.split('/')[0] for i in F_date]
day = [i.split('/')[1] for i in F_date]
year = [i.split('/')[2] for i in F_date]
print(month)
print(day)
print(year)
print(year, month, day)
comp_data = (year, month, day)
print(comp_data)


# a) Write a regular expression to extract the date.
# b) Capture the date in a variable f_date
# c) Split the date and store it as month, day, year
# d) Convert the date to date format year-month-day where month and day always have 2 digits. Save the
#    result in comp_date
# e) Print comp_date

print (solution_separator)

#) Extra Credit:
s8 = "These are some dates: 1/23/2011, 2/1/2006, 12/31/2007, 9/15/1993, 04/23/1797."

# a) Use a regex to collect the dates into a list
# b) Use the code above to convert them into yyyy-mm-dd format.
