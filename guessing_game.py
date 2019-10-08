#!/usr/bin/env python3

# Created by DJ Watson
# Created on September 2019
# this program is a guessing game where the user has to guess a number
# that the system has in memory


import random

random = random.randint(1, 9+1)


def main():
    # input

    numinput = input("Guess the number I am thinking of (0-9): ")
    # process and output

    try:
        intcheck = int(numinput)
        if int(numinput) == random:
            print("")
            print("Correct!")

        else:
            print("")
            print("Incorrect!")
            print("The number is {}".format(random))
    except ValueError:
        print("")
        print("Invalid input")


if __name__ == "__main__":
    main()
