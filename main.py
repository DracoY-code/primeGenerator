"""
Author: DracoY
File: main.py

This is the main file application.
"""

import generator
import time

def main():
    print("Please enter the number of primes to be generated...")
    lim = int(input("::> "))
    print()

    genObject = generator.prime_Generator(lim)

    for i in genObject:
        print(i)
        time.sleep(0.01)

    print("\n" + "The End")


if __name__ == "__main__":
    main()
