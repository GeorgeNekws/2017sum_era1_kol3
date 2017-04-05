# GeorgeNekws

import unittest
from code import Matrix

class test_matrix_operations(unittest.TestCase):
	def setUp(self):
		self.obj = Matrix()
	
	def test_add_between_matrces(self):
		self.assertEqual([3, 3, 3, 3] , self.obj.addition([1, 1, 1, 1] , [2, 2, 2, 2]) )

	def test_add_between_matrix_and_scalar(self):
		self.assertEqual([6, 6, 6, 6] , self.obj.addition([1, 1, 1, 1] , [5]) )	

	def test_add_between_scalar_and_matrix(self):
		self.assertEqual([6, 6, 6, 6] , self.obj.addition( [5], [1, 1, 1, 1]) )	



	def test_subtract_between_matrces(self):
		self.assertEqual([1, 1, 1, 1] , self.obj.subtraction([2, 2, 2, 2] , [1, 1, 1, 1])

	def test_subtract_between_matrix_and_scalar(self):
		self.assertEqual([4, 4, 4, 4] , self.obj.subtraction([5] , [1, 1, 1, 1])

	def test_subtract_between_scalar_and_matrix(self):
		self.assertEqual([-4, -4, -4, -4] , self.obj.subtraction([1, 1, 1, 1] , [5])

if __name__ == '__main__':
	unittest.main()
