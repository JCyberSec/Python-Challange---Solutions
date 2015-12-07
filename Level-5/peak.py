#!/usr/bin/python
# -*- coding: utf-8 -*-
import cPickle as pickle

dict1 = pickle.load(open('message1.pkl', 'rb'))

for i in dict1:
    for j in i:
        for k in range(j[1]):
            print j[0],

			
