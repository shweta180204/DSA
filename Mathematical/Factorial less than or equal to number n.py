'''A number n is called a factorial number if it is the factorial of a positive integer. For example, the first few factorial numbers are 1, 2, 6, 24, 120,
Given a number n, the task is to return the list/vector of the factorial numbers smaller than or equal to n.

Examples:

Input: n = 3
Output: 1 2
Explanation: The first factorial number is 1 which is less than equal to n. The second number is 2 which is less than equal to n,but the third factorial number is 6 which is greater than n. So we print only 1 and 2.
'''



def Factorial(n):
    result=[]
    i=1
    fact=1
    while fact<=n:
        result.append(fact)
        i+=1
        fact*=i
        
    return result

n=int(input("enter a number "))
print(Factorial(n))
