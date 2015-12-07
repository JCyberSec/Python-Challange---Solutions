#!/usr/bin/python
# -*- coding: utf-8 -*-

from string import maketrans

intab = 'abcdefghijklmnopqrstuvwxyz'
outtab = 'cdefghijklmnopqrstuvwxyzab'
trantab = maketrans(intab, outtab)

str = 'pc/def/map.html'
print str.translate(trantab)

			
