#!/usr/bin/env python3
"""
 Implementation (c) 2016,2017 Brig Young (github.com/Sonophoto)
 License: BSD-2c, i.e. Cite.

 Demonstrate the actual algorythm of Euclid in such a manner that
 Gabriel Lame's Modification is a trivial modification of the
 function. Both versions conform with the definition of gcd()
 in "Concrete Mathematics" Graham, Knuth, Patashnik. pp. #TODO

 An in depth discussion of the relationship of the Euclid algo
 and the Gabriel Lamé modification (and proof) may be found here:

 http://www.cut-the-knot.org/blue/LamesTheorem.shtml
"""

def gcd_euclid(a, b):
    """ Calculate gcd using Euclid original algorithm from Elements VII.2
    
    """
    if (a <= 0 and b <= 0):         # gcd(0,0) is UNDEFINED
       return("NaN")
    if (a == 0 or b == 0):          # gcd([0,1|1,0]) by definition
       return (0)
    while (a != b):                 # reduce until a == b
        if (a > b):                 #
            if (b == 0):            #
                return (a)          # a == b at last reduction
            a = a - b               #
        else:                       #
            if (a == 0):            # b == a at last reduction
                return (b)          #
            b = b - a               #
    return a                        #

def gcd_lame(a, b):
    """
    Calculate gcd using Gabiel Lame's mod-ification of Euclids algorithm
    """

    if (a <= 0 and b <= 0):
        return("NaN")
    if (a == 0 or b == 0):
        return (0)
    while (a != b):
        if (a > b):
            if (b == 0):
                return (a)
            a = a % b               # use mod operator not subtraction
        else:
            if (a == 0):
                return (b)
            b = b % a               # ditto
    return a

