# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 22:02:14 2020

@author: Administrator
"""

f = open("ldif.txt", "r")
newf = open("ldif_.txt","a")
space = 0
for line in f:
    if "dn:" in line:
        s = line.split(",")
        if len(s) > 1:
            space = len(s) - 1
    else:
        line = '  '+line
    newline = line
    for id in range(space):
        newline = '  ' + newline
    print(newline)
    newf.write(newline)

f.close()
newf.close()