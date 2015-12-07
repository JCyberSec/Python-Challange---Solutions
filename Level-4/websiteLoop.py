#!/usr/bin/python
# -*- coding: utf-8 -*-
from urllib import *

number = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '0',
    ]
num = '12345'

for i in range(400):
    cont = True
    while cont:
        f = \
            urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
                     + num)
        num = ''
        contense = ''
        for f in f.read():
            contense = contense + f
            if f is 'Y':
                if f in number:
                    num = int(num + f) / 2
            elif f in number:
                num = num + f
        print contense
        cont = False


			
