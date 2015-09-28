__author__ = 'Shiatime'

import sys
import random
import math
from timeit import Timer

def approximate_pi(paths):
    counter = 0
    pie_sum = 0
    num_of_quadrants= 4
    while counter < paths:
        pie_sum += num_of_quadrants * math.sqrt(1-random.random()**2)
        counter+=1

    print("Approximation of pi with %s paths is %s" % (paths,pie_sum/paths))


def main():

    while True:

        num_of_paths = input("Enter the number of paths or q to quit: ")
        if num_of_paths =="q":
            break
        t = Timer(lambda: approximate_pi(int(num_of_paths)))
        print("Time Taken" % t.timeit(number=1))


if __name__ == "__main__":
    sys.exit(main())
