# Code : AP21110011577
# Name : Chukka Chanakya Devendra
# Question No. : 2
"""There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
 
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
 
Your score is the sum of the points of the cards you have taken.
 
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
 
Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
 
Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4
 
Example 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
"""



def ans(arr,k,n):
    cur=0
    max_p=0
    for i in range(k):
        cur+=arr[i]
    max_p=cur
    j=n-1
    for i in range(k-1,-1,-1):
        cur=(cur+arr[j]-arr[i])
        max_p=max(cur,max_p)
        j-=1
    return max_p

def main():
    arr=[]
    k=int(input("Enter value of k : "))
    arr=list(map(int,input("Enter the array elements separated by spaces : ").split(' ')))
    n=len(arr)
    print("The Max value that can be obtained is :",ans(arr,k,n))
main()




"""
OUTPUT FOR THE CODE FROM TERMINAL

------------------------------------------------------------------------------------------------------------

PS D:\VSCode\AP21110011577_Factwise_BE> python -u "d:\VSCode\AP21110011577_Factwise_BE\q2.py"
Enter the value of k: 3
Enter the array elements separated by spaces : 1 2 3 4 5 6 1
The Max value that can be obtained is : 12


PS D:\VSCode\AP21110011577_Factwise_BE> python -u "d:\VSCode\AP21110011577_Factwise_BE\q2.py"
Enter the value of k: 2
Enter the array elements separated by spaces : 2 2 2
The Max value that can be obtained is : 4


PS D:\VSCode\AP21110011577_Factwise_BE> python -u "d:\VSCode\AP21110011577_Factwise_BE\q2.py"
Enter the value of k: 7
Enter the array elements separated by spaces : 9 7 7 9 7 7 9
The Max value that can be obtained is : 55


PS D:\VSCode\AP21110011577_Factwise_BE> 

------------------------------------------------------------------------------------------------------------

"""