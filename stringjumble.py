"""
stringjumble.py
Author: Bauti G
Credit: Liam S.

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
string=str(input("Please enter a string of text (the bigger the better): "))
print('you entered "{0}". Now jumble it: '.format(string))
number=0
number2=0
number3=0

stringlist = list(string)
print(list("".join(stringlist)))

if stringlist[number]=' ':
    newlist[number3]=stringlist[number2:number]
    number2=number
    number=number+1
    number3=number3+1

print("".join(stringlist)[::-1])
"""
print("".join(stringlist2)[::-1])
"""