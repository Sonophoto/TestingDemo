#!/usr/bin/env python3

# Fibonacci Series:
# Implementation (c) 2016,2017 Brig Young (github.com/Sonophoto)
# License: BSD-2c, i.e. Cite.
#
# Reference for this Series: https://oeis.org/search?q=fibonacci
# OEIS: Online Encyclopedia of Integer Sequences
# F(n) = (F(n-1) + F(n-2) with F(0) == 0 and F(1) == 1
# F(0) = 0, F(1) == 1, F(2) == 1, F(3) == 2, F(4) == 3, ...

# Thanks to http://gozips.uakron.edu/~crm23/fibonacci/fibonacci.htm
# for the closed form of the Fibonacci sequence used in the generator.

import unittest
import fibonacci as fm

class test_Fibonacci(unittest.TestCase):
    """Test all Fibonacci functions against a list of known Fibonacci numbers
       Values indexed  0 - 38 are from OEIS https://oeis.org/search?q=fibonacci
                      39 - 50 manually calculated and verified by Brig Young
    """

    century_fib = 354224848179261915075
    """A curated value of fibonacci(100) ref: M.L. Hetland pp. 177.
       Note that Magnus is skipping the beginning zero so his indices are
       actually (N-1). Also see:
       http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable.html
    """

    fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,\
            610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,\
            46368, 75025, 121393, 196418, 317811, 514229, 832040,\
            1346269, 2178309, 3524578, 5702887, 9227465, 14930352,\
            24157817, 39088169, 63245986, 102334155, 165580141,\
            267914296, 433494437, 701408733, 1134903170, 1836311903,\
            2971215073, 4807526976, 7778742049, 12586269025]
    """A curated list of Fibonacci numbers with correctly matched indexes
    """

    def test_Sequencer(self):
        """Create a list of fibonacci numbers via sequencing over count of known
           good values and compare to list of known good values.
        """
        sequenced_list = []
        [sequenced_list.append(fm.fibonacciSequencer(x)) for x in range(len(self.fibs))]
        self.assertEqual(sequenced_list, self.fibs,\
        "fibonacciSequencer() has calculated incorrect values")

    def test_Generator(self):
        """Create a list of fibonacci numbers via a python generator indexed by
           count of known good values and compare to list of known good values.
        """
        generated_list = []
        fibgen = fm.fibonacciGenerator()
        [generated_list.append(next(fibgen)) for x in range(len(self.fibs))]
        self.assertEqual(generated_list, self.fibs,\
        "fibonacciGenerator() has caculated incorrect values")

    def test_ClosedForm(self):
        """Create a list of fibonacci numbers via closed form equation indexed by
           count of known good values and compare to list of known good values.
        """
        closedform_list = []
        [closedform_list.append(fm.fibonacciClosedForm(x)) for x in range(len(self.fibs))]
        self.assertEqual(closedform_list, self.fibs,\
        "fibonacciClosedForm() has calculated incorrect values")

    def test_NaiveRecursion(self):
        """Create a list of fibonacci numbers via naive recursion indexed by
           count of known good values and compare to list of known good values.
        """
        fibs_short_list = self.fibs[:20]
        recursion_list = []
        [recursion_list.append(fm.fibonacciNaiveRecursion(x)) for x in range(len(fibs_short_list))]
        self.assertEqual(recursion_list, fibs_short_list,\
        "fibonacciRecursion() has calculated incorrect values")

    def test_MemoRecursion(self):
        """Create a list of fibonacci numbers via recursion with a memo-ized
           cache of previously calculated values. The returned list of values
           are then compared to a list of known good values.
        """
        fibs_short_list = self.fibs[:20]
        memo_recursion_list = []
        [memo_recursion_list.append(fm.fibonacciMemoRecursion(x)) for x in range(len(fibs_short_list))]
        self.assertEqual(memo_recursion_list, fibs_short_list,\
        "fibonacciMemoRecursion() has calculated incorrect values")

    def test_DeepRecursion(self):
        """Evaluate Memo Recursion at N=100 and compared to known good result
        """
        self.assertEqual(fm.fibonacciMemoRecursion(100), self.century_fib,\
        "fibonacciMemoRecursion() has caluculated incorrect deep result")
 
unittest.main(verbosity=2)

