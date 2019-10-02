#Questão 1
import math  
def Q1():
	print("Para a equação ax^2 + bx + c, insira os valores de a, b e c, respectivamente.")
	a = int(input())
	b = int(input())
	c = int(input())
	Delta = ((b**2) - 4*a*c)
	x1 = 0
	x2 = 0
	if(Delta > 0):
		x1 = ((b*(-1)) + math.sqrt(Delta))/(2*a)
		x2 = ((b*(-1)) - math.sqrt(Delta))/(2*a)
		print("As raizes da equação são", x1, "e", x2)
		return (0)
	elif(Delta == 0):
		x1 = (b*(-1))/(2*a)
		print("A raiz da equação é", x1)
		return (0)
	else:
                #raizDelta = math.
		print("As raizes da equação são (", b, "+", math.sqrt(Delta*(-1)), \
                      "i)/", 2*a, "e (",b, "-", math.sqrt(Delta*(-1)), "i)/", 2*a)
		return 1
		
	i = input()

Q1()
