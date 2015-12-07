#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

f = open('text1.txt')
file1 = ''
for line in f:
    file1 = str(file1) + line.strip()

p = re.compile('[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}')
count = 0
for line in file1:
    match = re.findall(p, file1)
    field1 = match[count]
    print field1[4:5]
    count = count + 1


			
