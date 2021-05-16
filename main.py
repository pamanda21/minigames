import random

print("Welcome to my amazing dice rolling experience!")

while 1:
    print("How many dice do you want to roll?")

    try:
        n = int(input())

        if n < 1:
            raise Exception
        print("Now rolling {} dice!".format(n))

        def rolldice():
            print(random.randint(1, 6))

        for x in range(n):
            rolldice()

        print("Wow that was so much fun!!!!")
    except Exception:
        print("Please input a positive number")
