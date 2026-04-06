import random
name=str(input("hello, what is your name?: "))
print(f"ok, {name}. we will play a game of guessing a number.\n it will be between 1 and 100 including and there will be 10 tries")

num=random.randint(1, 100)
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")

for i in range(6):
    if i>=5:
        print("you lost!. the number was", num)
        break
    user=int(input("enter your guess: "))
    if user == num:
        print(f"you got the number in {i} tries!")
        break
    if user < num:
        print("number is too small")
    else:
        print("number is too large")

