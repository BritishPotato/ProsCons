# Welcome message.
print("Welcome to the Pros and Cons Decision Making Application", end="\n\n")

# Ask for the dilemma.
dilemma = input("Please write your dilemma: ")
print()

# Ask for pros and cons, add to pros and cons list, stop when exit is written.
print("Write your pros and cons")
print("If your statement is a pro, write 'pro' first, press ENTER, then write your arguments.")
print("If your statement is a con, write 'con' first, press ENTER, then write your arguments.")
print("If you wish to stop writing pros and cons, write 'exit', then press ENTER")
print()

pros = []
cons = []

current = ""

"""

"""

while current != "exit":
    while current != "pro" and current != "con":
        current = input("Please write whether your argument will be 'pro' or 'con': ")
    
    if current == "pro":
        while True:
            current = input("PRO argument with weight from 0-10 at the end: ")
            if current == "con" or current == "exit":
                break
            pros.append([current[:-2], int(current[-2:])])
    
    print()
    
    if current == "con":
        while True:
            current = input("CON argument with weight from 1-10 at the end: ")
            if current == "pro" or current == "exit":
                break
            cons.append([current[:-2], int(current[-2:])])

total = 0
abs_total = 0
print("Results:")
for pro, num in pros:
    print(pro, num)
    total += num
    abs_total += num


for con, num in cons:
    print(con, -num)
    total -= num
    abs_total += num

if total > 0:
    result = "PRO"
elif total == 0:
    result = "BALANCED"
elif total < 0:
    result = "CON"
print(result, "wins as the total is", total, "with a better margin of", abs(total) / abs_total * 100, "%")