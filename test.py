#!/usr/bin/env python
# coding:utf-8

# FileName: test.py
# Author: sesilvar
# Date: 2016-12-25

if __name__=='__main__':
    s=raw_input('please input something:')
    s1=[2,3,4,1]
    j=0
    k=0
    while k<len(s1):
        j=j+s1[k]
        k+=1
    print j

'''
    try:
        d=int(s)
        print 'Your input is "%d"'%d
    except:
        print 'please ensure your input is a number.'

    for i in range(0,d):
        print i

    j=0
    while j<=i:
        print j
        j=j+1

    if d>0:
        print "Your number is greater than 0"
    elif d<0:
        print "Your number is less than 0"
    else:
        print "Your number is equal to 0"
'''
