#!/usr/bin/env python3

import os
#os.popen('ls')
#os.popen('whoami')
#os.popen('ifconfig')

ls_return = os.popen('ls')
print('The contents of ls_return:',ls_return)
whoami_return = os.popen('whoami')
print('The contents of whoami_return:',whoami_return)
ifconfig_return = os.popen('ifconfig')
print('The contents of ifconfig_return:',ifconfig_return )
print('\n\n')


ipconfig_return = os.popen('ipconfig')
ipconfig_contents = ipconfig_return.read()
print('The contents of ipconfig_return:',ipconfig_contents)
