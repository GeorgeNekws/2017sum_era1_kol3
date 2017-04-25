# GeorgeNekws

import unittest
from matrix_module import Matrix
import math 

class test_matrix_operations(unittest.TestCase):
	def setUp(self):
		self.obj = Matrix([1, 1, 1, 1] , [2, 2, 2, 2])
		
	
	def test_add_between_matrices(self):
		self.assertEqual([3, 3, 3, 3] , self.obj.addition([1, 1, 1, 1] , [2, 2, 2, 2]) )

	def test_add_between_matrix_and_scalar(self):
		self.assertEqual([6, 6, 6, 6] , self.obj.addition([1, 1, 1, 1] , [5]) )	

	def test_add_between_scalar_and_matrix(self):
		self.assertEqual([6, 6, 6, 6] , self.obj.addition( [5], [1, 1, 1, 1]) )	
		
	def test_add_between_negative_scalar_and_matrix(self):
		self.assertEqual([-4, -4, -4, -4] , self.obj.addition( [-5], [1, 1, 1, 1]) )	


	def test_subtract_between_matrices(self):
		self.assertEqual([1, 1, 1, 1] , self.obj.subtraction([2, 2, 2, 2] , [1, 1, 1, 1]))

	def test_subtract_between_matrix_and_scalar(self):
		self.assertEqual([4, 4, 4, 4] , self.obj.subtraction([5] , [1, 1, 1, 1]))

	def test_subtract_between_scalar_and_matrix(self):
		self.assertEqual([-4, -4, -4, -4] , self.obj.subtraction([1, 1, 1, 1] , [5]))
		
		
		
	def test_multiplication_between_matrices(self):
		self.assertEqual([4, 4, 4, 4] , self.obj.multiplication([1, 1, 1, 1] , [2, 2, 2, 2]))
	
	def test_multiplication_between_negative_matrices(self):
		self.assertEqual([4, 4, 4, 4] , self.obj.multiplication([-1, -1, -1, -1] , [-2, -2, -2, -2]))	
		
	def test_multiplication_between_negative_and_positive_matrices(self):
		self.assertEqual([-4, -4, -4, -4] , self.obj.multiplication([1, 1, 1, 1] , [-2, -2, -2, -2]))	
		

	def test_multiplication_between_matrix_and_scalar(self):
		self.assertEqual([5, 5, 5, 5] , self.obj.multiplication([5] , [1, 1, 1, 1]))

	def test_multiplication_between_scalar_and_matrix(self):
		self.assertEqual([5, 5, 5, 5] , self.obj.multiplication([1, 1, 1, 1] , [5]))	

if __name__ == '__main__':
	unittest.main()
