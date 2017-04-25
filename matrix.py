#!/usr/bin/python
import matrix_module as mm

"""

matrix_1 = []
matrix_2 = []

print 'If you want to make an operation with a scalar press "q" after the insertion of the scalar'

print 'Give the elements of the first 2x2 matrix'

for i in range(4):
	input_num = raw_input('%d element : ' %i)
	
	if input_num == 'q':
		break
	else:	
		input_num = int(input_num)
		matrix_1.append(input_num)
		
print 'Give the elements of the second 2x2 matrix'

for i in range(4):
	input_num = raw_input('%d element : ' %i)
	
	if input_num == 'q':
		break
	else:	
		input_num = int(input_num)
		matrix_2.append(input_num)



operation = int(raw_input('Choose 1 for "addition" or 2 for "product" or 3 for "Subtraction" : '))

if operation == 1:
	
	print 'You chose addition\n'
	
	obj = mm.Matrix(matrix_1 , matrix_2)
	
	matrix_3 = obj.addition(matrix_1 , matrix_2)
	
	print "The result is :\n"
	print "| " + str(matrix_3[0]) + "  " + str(matrix_3[1]) + " |"
	print "| " + str(matrix_3[2]) + "  " + str(matrix_3[3]) + " |"
	

elif operation == 2:
	
	print 'You chose multiplication\n'
	
	obj = mm.Matrix(matrix_1 , matrix_2)
	
	matrix_3 = obj.multiplication(matrix_1 , matrix_2)
	
	print "The result is :\n"
	print "| " + str(matrix_3[0]) + "  " + str(matrix_3[1]) + " |"
	print "| " + str(matrix_3[2]) + "  " + str(matrix_3[3]) + " |"
	
else:
	
	print 'You chose Subtraction\n'
	
	obj = mm.Matrix(matrix_1 , matrix_2)
	
	matrix_3 = obj.subtraction(matrix_1 , matrix_2)

	print "The result is :\n"
	print "| " + str(matrix_3[0]) + "  " + str(matrix_3[1]) + " |"
	print "| " + str(matrix_3[2]) + "  " + str(matrix_3[3]) + " |"
	
"""

####################################################################################

# Case 1 : addition between 2 matrices
	
obj_1 = mm.Matrix([1, 1, 1, 1] , [2, 2, 2, 2])
	
matrix_3 = obj_1.addition([1, 1, 1, 1] , [2, 2, 2, 2])

m3 = "| " + str(matrix_3[0]) + "  " + str(matrix_3[1]) + " |\n" + "| " + str(matrix_3[2]) + "  " + str(matrix_3[3]) + " |\n"

print "Addition between 2 matrices"	
print "The result is :\n"
print m3
	
	
# Case 2 : addition between matrix and scalar
	
obj_2 = mm.Matrix([1, 1, 1, 1] , [5])
	
matrix_3 = obj_2.addition([1, 1, 1, 1] , [5])
	
m3 = "| " + str(matrix_3[0]) + "  " + str(matrix_3[1]) + " |\n" + "| " + str(matrix_3[2]) + "  " + str(matrix_3[3]) + " |\n"

print "Addition between matrix and scalar"
print "The result is :\n"
print m3


# Case 3 : addition between scalar and matrix
	
obj_3 = mm.Matrix([5] , [1, 1, 1, 1])
	
matrix_3 = obj_3.addition([5] , [1, 1, 1, 1])

m3 = "| " + str(matrix_3[0]) + "  " + str(matrix_3[1]) + " |\n" + "| " + str(matrix_3[2]) + "  " + str(matrix_3[3]) + " |\n"

print "Addition between scalar and matrix"
print "The result is :\n"
print m3


# Case 4 : subtraction between matrices
	
obj_4 = mm.Matrix([2, 2, 2, 2] , [1, 1, 1, 1])
	
matrix_3 = obj_4.subtraction([2, 2, 2, 2] , [1, 1, 1, 1])

m3 = "| " + str(matrix_3[0]) + "  " + str(matrix_3[1]) + " |\n" + "| " + str(matrix_3[2]) + "  " + str(matrix_3[3]) + " |\n"

print "Subtraction between matrices"
print "The result is :\n"
print m3


# Case 5 : subtraction between scalar and matrix
	
obj_5 = mm.Matrix([5] , [1, 1, 1, 1])
	
matrix_3 = obj_5.subtraction([5] , [1, 1, 1, 1])

m3 = "| " + str(matrix_3[0]) + "  " + str(matrix_3[1]) + " |\n" + "| " + str(matrix_3[2]) + "  " + str(matrix_3[3]) + " |\n"

print "Subtraction between scalar and matrix"
print "The result is :\n"
print m3

# Case 6 : subtraction between matrix and scalar
	
obj_6 = mm.Matrix([1, 1, 1, 1] , [5])
	
matrix_3 = obj_6.subtraction([1, 1, 1, 1] , [5])

m3 = "| " + str(matrix_3[0]) + "  " + str(matrix_3[1]) + " |\n" + "| " + str(matrix_3[2]) + "  " + str(matrix_3[3]) + " |\n"

print "Subtraction between matrix and scalar"
print "The result is :\n"
print m3


# Case 7 : multiplication between 2 matrices
	
obj_7 = mm.Matrix([1, 1, 1, 1] , [2, 2, 2, 2])
	
matrix_3 = obj_7.multiplication([1, 1, 1, 1] , [2, 2, 2, 2])

m3 = "| " + str(matrix_3[0]) + "  " + str(matrix_3[1]) + " |\n" + "| " + str(matrix_3[2]) + "  " + str(matrix_3[3]) + " |\n"

print "Multiplication between 2 matrices"	
print "The result is :\n"
print m3

