'''
Author -> Al-Imran Rony (2015331531)
Graphics Assignment 04
Mid-Point Circle Drawing Algorithm 
'''

def midPointCircleDraw(xc, yc, radius): 
	x, y = radius, 0 	
	
	print("(", x + xc, ", ", y + yc, ")", sep = "", end = "") 
	
	if (radius > 0) : 	
		print("(", x + xc, ", ", -y + yc, ")", sep = "", end = "") 

		print("(", y + xc, ", ", x + yc, ")", sep = "", end = "") 

		print("(", -y + xc, ", ", x + yc, ")", sep = "") 
	 
	P = 1 - radius 

	while (x > y): 	
		y += 1
		 
		if P <= 0: 						# Mid-point inside or on the perimeter
			P = P + 2 * y + 1 
		else:		 					# Mid-point outside the perimeter
			x -= 1
			P = P + 2 * y - 2 * x + 1
		
		if (x < y): 					# When all the perimeter points 
			break						# have been printed already
		
		# Printing the generated point its reflection in the other octants after translation 
		print("(", x + xc, ", ", y + yc, ")", sep = "", end = "") 

		print("(", -x + xc, ", ", y + yc, ")", sep = "", end = "") 

		print("(", x + xc, ", ", -y + yc, ")", sep = "", end = "") 

		print("(", -x + xc, ", ", -y + yc, ")", sep = "") 
		
		if x != y: 		
			print("(", y + xc, ", ", x + yc, ")", sep = "", end = "") 

			print("(", -y + xc, ", ", x + yc, ")", sep = "", end = "") 

			print("(", y + xc, ", ", -x + yc, ")", sep = "", end = "") 

			print("(", -y + xc, ", ", -x + yc, ")", sep = "") 
							
 
if __name__ == '__main__': 
	 
	midPointCircleDraw(0, 0, 3)    # To draw a circle of radius 3 centred at (0, 0)
