#!/usr/bin/python
# -*- coding: utf-8 -*-

import zipfile
import re

num = '90052'
comment = ''
try:
    with zipfile.ZipFile('channel.zip', 'r') as myzip:
        while True:
            contents = myzip.open(num + '.txt', 'r').read()
            num = re.findall('[0-9]+', contents)[0]
            filename = num + '.txt'
            info = myzip.getinfo(filename)
            comment = comment + info.comment
            print info.filename,
            print '\t\tComment:\t\t', info.comment
except IndexError:
    print comment
