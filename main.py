#Lesson 20 :

#Example 1:
x=1
while x<10:
    print(f"{x} is smaller than 10")
    x += 1

#Example 2 :write a program that countsdown from 10 to BLASTOFF!
t=10
while t>0:
    print(t)
    t-=1
print("BLASTOFF!")

#Example 3 : write a program that asks the user for a natural number N and then print all the factors.
N = int(input("N:"))
x=1
print("Factors:")
while x <=N:
    if N % x ==0:
        print(x)
    x += 1

#Example 4 : write a program that asks for a number from 1 to 20 but it keeps asking until you give it the correct number
x = int (input("Give me a number from 1 to 10:"))
while x <1 or x>10:
    print("No , it is not between 1 and 10.")
    x = int(input("Give me a number from 1 to 10:"))
print('that is good')

#Example 5 :
small = int (input("Give me a small number:"))
large = int (input("Give me a large number:"))
remainder = large % small
while remainder != 0:# while not remainder == 0:
    large = small
    small = remainder
    remainder = large % small
print(small)
