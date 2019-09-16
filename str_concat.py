# -*- coding: utf-8 -*-
"""
@author : yKRSW
@purpose: Sample of string concat
"""

var1 = "AAA"
print("var1 is " + var1)
#var1 is AAA

var2 = "BBB"
var3 = "CCC"
print("var2 is " + var2 + ", " + "var3 is " + var3)
#var2 is BBB, var3 is CCC

var2 = "BBB"
var3 = "CCC"
print("var2 is {}, var3 is {}".format(var2, var3))
#var2 is BBB, var3 is CCC

var1 = "AAA"
var2 = "BBB"
var3 = "CCC"
print("var2 is {v2}, var3 is {v3}. And var1 is {v1}, var2 is {v2}.".format(v1=var1, v2=var2, v3=var3))
#var2 is BBB, var3 is CCC. And var1 is AAA, var2 is BBB.