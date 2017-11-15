#!/usr/bin/env python3
""" Test app for Fibonacci and GCD functions
"""

import cherrypy
import fibonacci as fib
import gcdVersions as gcd
# import test_fibonacci
# import test_gcdVersions



class MVC_Cherry(object):
    """ Main Application Class for Fibonacci and GCD testing system
    """

    # Path is http://[ADDRESS]:[PORT]/FibonacciAPI?fidx=[INTEGER]
    @cherrypy.expose
    def FibonacciAPI(self, fibx=0):
        """ This is the view function for the fibonacci API 
        """
        if fibx is None:
            return "Error: Specify a value for fibx"
        fibx = int(fibx) # cast URL string to int...
        if (fibx > 1000): return "Error: Use a value <= 1000"
        if (fibx < 0): return "Error: Input value must be >= 0"
        fib_string = str(fib.fibonacciSequencer(fibx))
        return fib_string

    # Path is http://[ADDRESS]:[PORT]/gcdAPI?a_value=[INTEGER]&b_value=[INTEGER]
    @cherrypy.expose
    def gcdAPI(self, a_value=1, b_value=1):
        """ This is the view function for gcd API
        """
        if a_value is None or b_value is None:
            return "Error: Specify values for a_value and b_value"
        a_value = int(a_value)
        b_value = int(b_value)
        if a_value < 0 and b_value < 0 : return "Error: values must be greater than zero"
        gcd_string = str(gcd.gcd_lame(a_value, b_value))
        return gcd_string 


if __name__ == "__main__":
    cherrypy.quickstart(MVC_Cherry(), '/')
    """ Starts internal httpd and listens at: http://127.0.0.1:8080 or whatever
        Heroku returns...
    """


