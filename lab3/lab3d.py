#!/usr/bin/env python3

#Author ID: warmastergenral

import subprocess

def free_space():
    p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    output = p.communicate()
    # The above stdout is stored in bytes
    # Convert stdout to a string and strip off the newline characters
    stdout = output[0].decode('utf-8').strip()
    return(stdout)

print(free_space())
