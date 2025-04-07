#!/bin/python3

import math
import os
import random
import re
import sys


#n = int(input().strip())
n = random(1,100)
# the strip() remove any spave in the input so we can make shure that its clean
if n%2 != 0:
    print("Weird")
else:
#to finish this you start with else the if so we wont write it every time thats why we write elife its like a short cute 
    if n >=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")
#its a good start me step by step insha2lah you can staart taking your time 