#!/usr/bin/env python3

#Author: Pouyan
#Author ID: warmastergenral
#Date Created: 2021/08/06

import sys

if len(sys.argv) == 2 :
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0 :
    print(timer)
    timer -= 1

print('blast off!')
