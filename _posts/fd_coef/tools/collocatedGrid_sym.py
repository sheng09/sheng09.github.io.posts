#!/usr/bin/env python3
from fractions import Fraction as frac
import sys

def factorial( N ):
    """
    Calculate N! = 1*2*3*4*...*N
    """
    value = N;
    for i in range(1,N):
        value = value * i
    return value


class vander_collocated_sym:
    """
    Calculate the solution of vandermonde equation for SYMMETRIC finite difference(FD) 
    scheme of COLLOCATED grid. FD coefficients will be calculated for points that are 
    NOT in the boundary region.

        Vandermonde equation for SYMMETRIC FD is:
            Ax = b
        while x = C[1], C[2], C[3], ..., C[N], and FD order is 2N.
        This equation is solve in (http://sheng09.github.io/2016/10/15/vandermonde/).

        FD coefficients for f'(x) and f''(x) are derived from x.
        f'(x) = d1[1] * { f(x+ dx) - f(x- dx) } +
                d1[2] * { f(x+2dx) - f(x-2dx) } +
                ...

        f"(x) = d2[1] * { f(x+ dx) + f(x- dx) - 2f(x) }+
                d2[2] * { f(x+2dx) + f(x-2dx) - 2f(x) }+
                ...
        Find details about symmetric FD in (http://sheng09.github.io/2016/10/13/finite-difference/)

    Attributes:
        order: FD order(should be an EVEN number).
        N    : equals to order/2.
        C    : result of the vandermonde equation Ax = b.
                NOTE: C[0] is not used. and length of C is (N+1).
        d1   : FD coefficients for f'(x).
                NOTE: d1[0] is not used. and length of d1 is (N+1).
        d2   : FD coefficients for f''(x).
                NOTE: d2[0] is not used. and length of d2 is (N+1).
    """
    def __init__(self, order):
        self.order = order
        self.N     = int(self.order/2)
        self.C     = [None,] * (self.N+1)
        self.d1    = [None,] * (self.N+1)
        self.d2    = [None,] * (self.N+1)
        self.vander_sol()
        #self.first_order()
        #self.second_order()
    def __str__(self):
        str = '\n  FD %dth order accuracy\n' % ( self.order )
        str = str + '[i]: %8s, %8s, %8s \n' %('Ci', 'f\'(x)', 'f\"(x)')
        for i in range( 1, self.N+1):
            str = str + '[%d]: %8s, %8s, %8s \n' % (i, self.C[i], self.d1[i], self.d2[i])
        return str
    def b(self, i):
        """Calculate the b[i].

        Args:
            i: row number.
        """
        if i == 1:
            return 1;
        numer = factorial( i-1 ) * factorial(i)
        denom = factorial(2*i-1)
        if (i-1)&1 == 1: #just even or odd
            numer = -numer
        return frac(numer, denom)
    def a(self, i, j):
        """Calculate the A[i][j].

        Args:
            i: row number.
            j: column number.
        """
        numer = i * factorial(j+i-1)
        denom = j * factorial(2*i-1) * factorial(j-i)
        return frac(numer, denom)
    def c(self, i):
        """Calculate the C[i] value from C[i+1],C[i+2],...,C[N].

        Args:
            i: row number.
        """
        value = self.b(i)
        if i == self.N:
            return value
        else:
            for j in range(i+1, self.N+1):
                value = value - self.a(i,j) * self.C[j]
            return value
    def vander_sol(self):
        """Calculate C. ( C[1],C[2],...C[order/2] ).
        """
        for i in range( self.N, 0, -1):
            self.C[i] = self.c(i)
        self.ok = True
    def fd1_coef(self, dx):
        """Calculate d1 given grid step(dx), which is used for f'(x) FD.

        Args:
            dx: grid step.
        Return:
            self.d1: coefficients for f'(x).
        """
        for i in range(1,self.N+1):
            self.d1[i] = self.C[i] / 2 / i /dx;
        return self.d1
    def fd2_coef(self, dx):
        """Calculate d2 give grid step(dx), which is used for f"(x) FD.

        Args:
            dx: grid step.
        Return:
            self.d2: coefficients for f"(x).
        """
        for i in range(1,self.N+1):
            self.d2[i] = self.C[i] / i / i /dx;
        return self.d2
    def markdown_row(self, ncol, which):
        """Generate the markdown table row for this order FD.

        Args:
            ncol:   number of column for the table.
            which:  which coefficients to be place in the table.
                    should be 'C','c' or 'f'.
                    'C': solution of vandermonde equation.
                    'c': d1, coefficients for f'(x) FD.
                    'f': d2, coefficients for f"(x) FD.
        """
        if which == 'C':
            dat = self.C
        elif which == 'c':
            dat = self.d1
        elif which == 'f':
            dat = self.d2
        line = '|%d|' % (self.N*2)
        for i in range(1,self.N+1):
            line = line + ' $%s$ |' % (dat[i])
        for i in range(1,ncol - self.N+1):
            line = line + ' |'
        line = line + '\n'
        return line

class vander_collocated_sym_table(object):
    """
    Generate markdown table given max FD order.

    Args:
        maxorder:   max FD order.
        N:          equals to maxorder/2.
    """
    def __init__(self, maxorder):
        self.maxorder = maxorder
        self.orders = range(2, maxorder+2, 2)
        self.maxN = int( maxorder/2 )
        self.dat = {}
        for o in self.orders:
            self.dat[o] = vander_collocated_sym(o)
            #print(self.dat[o])
            self.dat[o].fd1_coef(1)
            self.dat[o].fd2_coef(1)
    def markdown_table(self, which):
        """
        Generate the table for FD order of 2, 4, 6 ,..., maxorder.

        Args:
            which:  which coefficients to be place in the table.
                    should be 'C','c' or 'f'.
                    'C': solution of vandermonde equation.
                    'c': d1, coefficients for f'(x) FD.
                    'f': d2, coefficients for f"(x) FD.
        """
        if which == 'C':
            coef = 'C'
        elif which == 'c':
            coef = 'c'
        elif which == 'f':
            coef = 'f'
        table = '|order|'
        for i in range(1,self.maxN+1):
            table = table + '$%s_{%d}$ |' % (coef,i)
        table = table + '\n|'
        for i in range(1,self.maxN+1):
            table = table + '-|'
        table = table + '\n'
        for o in self.orders:
            table = table + (self.dat[o]).markdown_row(self.maxN, which)
        return table

#class fd_sym_1(vander_collocated_sym):
#    """Generate the coefficients for 1st order symmetric FD
#    """
#    def __init__(self, order,dx):
#        N = int(order/2)
#        vander.__init__(self,N)
#        self.all_c()
#        self.first_order()
#        """coefficients
#        """
#        self.coef = [float(c) for c in self.d1][1:]
#
#class fd_sym_2(vander_collocated_sym):
#    """Generate the coefficients for 2st order symmetric FD
#    """
#    def __init__(self, order,dx):
#        N = int(order/2)
#        vander.__init__(self,N)
#        self.all_c()
#        self.second_order()
#        """coefficients
#        """
#        dx2 = dx * dx
#        self.coef = [float(c)/dx2 for c in self.d2][1:]
#

if __name__ == '__main__':
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) ==2:
        order = eval(sys.argv[1])
        v = vander_collocated_sym(order)
        v.vander_sol()
        v.fd1_coef(dx = 1)
        v.fd2_coef(dx = 1)
        print(v)
    elif len(sys.argv) == 3:
        which = (sys.argv[2])
        maxorder = eval(sys.argv[1])
        table = vander_collocated_sym_table(maxorder)
        print( table.markdown_table(which) )
