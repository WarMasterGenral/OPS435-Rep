#!/usr/bin/env python3

import sys

print('version: ', sys.version,'\n') # tells us the version of the python currently in use
print('platform: ', sys.platform,'\n') # tells us our operating system platform
print('sys.argv: ', sys.argv,'\n') # tells us a list of all items given at the command line when running our python script from a command shell
print(len(sys.argv)) # tells us the number of command line arguments the user provide from a command shell
sys.exit() # will immediately end the running Python script, ignoring the remaining lines in the Python script
