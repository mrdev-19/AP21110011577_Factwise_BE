# Code : AP21110011577
# Name : Chukka Chanakya Devendra
# Question No. : 1
"""
If the numbers to are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
 
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def dev():
    char_sd = (0, 3, 3, 5, 4, 4, 3, 5, 5, 4)  
    char10_19 = (0, 3, 6, 6, 5, 5, 5, 7, 6, 6) 
    char20_99 = (0, 6, 6, 8, 8, 7, 7, 9, 8, 8) 
    char_thou = (7, 10, 11)
    let_1_99 = (sum(char_sd) * 9 + char10_19[1] +
                                sum(char20_99) + sum(char10_19[2:]) * 10) * 10 
    let_100_999 = char_thou[0] * 9 + char_thou[1] * 99 * 9 + sum(char_sd) * 100
    total_letters = let_1_99 + let_100_999 + char_thou[2]
    return total_letters
print(dev())



"""
TERMINAL OUTPUT:

------------------------------------------------------------------------------------------------------------

PS D:\VSCode\AP21110011577_Factwise_BE> python -u "d:\VSCode\AP21110011577_Factwise_BE\q1.py"
21124

PS D:\VSCode\AP21110011577_Factwise_BE> 

------------------------------------------------------------------------------------------------------------

"""