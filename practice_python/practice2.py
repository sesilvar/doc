#!/usr/bin/env python
# coding:utf-8

# FileName: practice2.py
# Author: sesilvar
# Date: 2016-12-27

from sys import argv

def two_1():
    in1=raw_input("please input something:")
    print in1
    print "Your input is %s"%in1

def two_2():
    in2=1+2*4
    print in2
    print "The result is %d"%in2

def two_4():
    in4=raw_input("please input something:")
    try:
        out4=int(in4)
        print "Your number is %d."%out4
    except:
        out4=str(in4)
        print "Your input is %s."%out4

def two_5():
    count5_1=0
    while count5_1<11:
        print count5_1
        count5_1+=1
    for count5_2 in range(11):
        print count5_2

def two_6():
    in6=raw_input("Please input a number:")
    try:
        out6=float(in6)
        if out6>0:
            print "The number is greater than 0"
        elif out6<0:
            print "The number is less than 0"
        else:
            print "The number is equal to 0"
    except:
        print "Your input is incorrect."

#def two_7():

def main():
    main="two_%s"%str(argv[1])
    print main
    try:
        exec("%s()"%main)
    except:
        print "Sorry,there is no %s"%main

if __name__=="__main__":
    main()
