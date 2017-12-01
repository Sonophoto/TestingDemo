#!/usr/bin/env python3
""" Test API for Fibonacci and GCD functions
"""
import cherrypy
import fibonacci as fib
import gcdVersions as gcd
# import test_fibonacci
# import test_gcdVersions


class Fib_GCD_API(object):
    """ Main Application Class for Fibonacci and GCD testing system
    """

    @cherrypy.expose
    def index(self):
        return \
"""
<html><head></head>
  <body>
    <h1>Choose a Function API</h1>
    <p><a href="FibonacciAPI">Fibonacci API</a></p>
    <p><a href="gcdAPI">Greatest Common Divisor API</a></p>
  </body>
</html>
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

    import os as os

    conf = {
        'global': {
            'server.socket_host': '0.0.0.0',
            'server.socket_port': int(os.environ.get('PORT', 8080))
        },
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }

    }

    """ Starts internal httpd and listens at whatever Heroku returns...
    """
    cherrypy.quickstart(Fib_GCD_API(), '/', conf)

