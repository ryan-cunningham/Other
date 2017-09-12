# LPTHW: Exercise 33 - While Loops

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The Numbers: ")

for num in numbers:
    print(num)

    
    
########################
##### study drills #####
########################

def listgen(hi, step):
    for i in range (0, hi, step):
        numbers.append(i)


hi = int(input("What is our range? (start point is 0): "))
step = int(input("And the step-size?: "))

numbers = []

listgen(hi, step)

print("The numbers:")

for num in numbers:
    print(num)
