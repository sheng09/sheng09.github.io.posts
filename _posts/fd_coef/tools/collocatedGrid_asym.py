#!/usr/bin/env python3
import sys
import numpy as np
from scipy.linalg import solve
from fractions import Fraction as frac

class vander_collocated_asym:
	"""
	Calculate the solution of vandermonde equation for ASYMMETRIC finite difference(FD) scheme of COLLOCATED grid.
    FD coefficients will be calculated for points that are IN THE BOUNDARY REGION.

		Vandermonde equation for ASYMMETRIC FD is:
			Ax = b
		while x = C[1], C[2], C[3], ..., C[N], and FD order is 2N.
		This equation is solve in (http://sheng09.github.io/2016/10/15/vandermonde/).

	Find details about asymmetric FD in (http://sheng09.github.io/2016/10/17/finite-difference-asymmetric).

			[  boundary region  ]
			*---*---*---*---*---*--...
			0   1   2   3   4   5

	Attributes:
		order:		FD order(should be an EVEN number).
		N:			equals to order/2.
					N is number of points in the boundary region.
		nboundary:  number of points that located in the boundary region.
		C:          result of vandermonde equation.
						C[0] is for 0th point in the boundary region.
						C[1] ..     1st ..
						...
	"""
	def __init__(self,order):
		self.order = order
		self.N = order
		self.nboundary = int(self.N/2)
		self.C = {}
		self.d1 ={}
	def matrix_b(self):
		"""
		Calculate the b matrix for boundary point k.

		Return:
			b in numpy.array format.
		"""
		b = [1,]
		b = b + [0,]*(self.N-1)
		return np.array(b)
	def row_a(self, i, k):
		"""
		Calculate row[i] for A matrix for boundary point k.

		Args:
			i: row number
			k: point position in the boundary region.

		Return:
			the ith row of A in numpy.array formate.
		"""
		row1 = [ j**i for j in range(-k,0) ]
		row2 = [ j**i for j in range(1,self.N-k+1)]
		return np.array( row1 + row2 )
	def matrix_A(self, k):
		"""
		Calculate the A matrix for boundary point k

		Args:
			k: point position in the boundary region.
		Return:
			A in np.array formate.
		"""
		A = [self.row_a(i,k) for i in range(0,self.N)]
		return np.array(A)
	def vander_sol_k(self,k):
		"""
		Solve the vandermonde equation for boundary point k.

		Args:
			k: point position in the boundary region.

		Return:
			solution for kth point.
		"""
		A = self.matrix_A(k)
		b = self.matrix_b()
		x = solve(A,b)
		return x
	def vander_sol_all(self):
		"""
		Solve al the vandermonde equation for all the points in the boundary.
		"""
		for i in range(0, int(self.N) ):
			self.C[i] = self.value_k(i)
		return self.C
	def __str__(self):
		mat = '%4s\n' % 'k'
		for irow,row in enumerate(self.C):
			line ='%4d' % irow
			for item in row:
				line = line + '%12f' %(item)
			mat = mat + line + '\n'
		return mat
	def fd1_coef(self, dx, nx):
		"""Calculate d1 given grid step(dx) and number of points(nx), which is used for f'(x) FD.

        Args:
            dx: grid step.
            nx: number of points
        Return:
            self.d1: coefficients for f'(x).
        """
        for k in range(0, self.nboundary ):
			row1 = {}
			#row2 = {}
			for j in range(-k, 0):
				row1[j] = self.C[k][j+k] / dx / j
			for j in range(1, self.order-k+1):
				#print(len(self.C))
				row1[j] = self.C[k][j+k-1] /dx /j
			self.coef[k] = row1
			self.coef[nx-1-k] = row1
        pass

class fd_asym_1(vander_collocated_asym):
	"""Generate the coefficients for 1st order symmetric FD
    """
	def __init__(self,order,dx,nx):
		vander_asym.__init__(self,order)
		self.value_all()
		"""coefficients
        """
		self.coef = {}
		for k in range(0, self.nboundary ):
			row1 = {}
			#row2 = {}
			for j in range(-k, 0):
				row1[j] = self.C[k][j+k] / dx / j
			for j in range(1, self.order-k+1):
				#print(len(self.C))
				row1[j] = self.C[k][j+k-1] /dx /j
			self.coef[k] = row1
			self.coef[nx-1-k] = row1
        #for item in self.coef:
        #	for 
		#for irow,row in enumerate(self.C):
		#	for j in range(-irow,0):
		#		self.C[irow][j+irow] = self.C[irow][j+irow] /dx/j
		#	for j in range(1,self.order-irow+1):
		#		self.C[irow][j+irow-1] = self.C[irow][j+irow-1]/dx/j
		#self.coef = self.C


class vander_asym_table(vander_asym):
	"""Generate the markdown table of FD coefficients for boundary points given order self.N
	"""
	def __init__(self,N):
		vander_asym.__init__(self,N)
		self.value_all()
	def markdown_table(self):
		"""Generate the table
		"""
		table = '|point k' + ' |'*(self.N+1) + '\n'
		table = table + '|' + '-|'*(self.N+1) + '\n'
		for row in range(0, int(self.N/2) ):
			table = table + self.markdown_row(row)
		return table
	def markdown_row(self,k):
		"""Generate the row(k) of table
		"""
		line = '| %d |' % (k)
		for j in range(-k,0,1):
			line = line + '$ C^%d_{(%d)(%d)} = %s  $|' %(k,self.N,j, ( self.C[k][j+k] ) )
		for j in range(1,self.N-k+1):
			line = line + '$ C^%d_{(%d)(%d)} = %s $|' %(k,self.N,j,  (self.C[k][j+k-1]) )
		line = line + '\n'
		return line


if __name__ == '__main__':
	N = eval(sys.argv[1])
	fd = vander_asym(N)
	fd.value_all()
	print(fd)

	table = vander_asym_table(N)
	print(table.markdown_table())
