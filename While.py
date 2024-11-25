#Martin C
#November 21, 2024

#problem 1: Write an infinite loop that prints “Infinite”. An infinite loop never ends. The
#condition is always true. After you prove to yourself that this works, comment out the code that
#produces the infinite loop. To break a loop in progress you should be able to do ctrl-C or
#command-C (depending on your platform).
i = 9
while True:
    print("infinite")
    i -= 1 #I added this part so the loop stops and runs the next line of code.
    if i != 10:
        break

#The following code produces the loop:
#i = 10
# while True:
#    print("infinite")

#problem 2: Create a list called L that starts with the numbers 57 and 83 in it. Then build a while
#loop, starting with a counter assigned to the value 0. On each iteration, the loop should append
#the current value of a counter variable to the list and then increase the counter by 1. The while
#loop should stop once the counter variable is greater than 10. Finish by printing a statement
#that tells us a) how many elements are in the list, and b) what the third element in the list is.

L = [57, 83]
counter = 0
while counter <=10:
    L.append(counter)
    counter +=1
print(f"there are {len(L)} elements in the list. The third element is: {L[2]}")
print(L) #I printed the list to verify that the while loop is working correctly.

#Problem 3: Using a while loop, ask the user to enter a number. Append each entered number
#to a list and add them together. Continue asking for a number until the sum of the list of
#numbers is greater than 100.

L_num = []
sum = 0
while sum <= 100:
    num = int(input("enter a number: "))
    L_num.append(num)
    sum += num
print("The sum is greater than 100") #The loop will continue to run until the sum is greater than 100.