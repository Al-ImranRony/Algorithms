'''
Author -> Al-Imran Rony (2015331531)
Graphics Assignment 05
Mid-Point Ellipse Drawing Algorithm 
'''

def midPointEllipse(rx, ry, xc, yc): 
	x, y = 0, ry 
    
    # Initial decision parameter of region 1
	d1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx))
	dx = 2 * ry * ry * x
	dy = 2 * rx * rx * y 

	while (dx < dy):                        	# For region 1 
		print("(", x + xc, ",", y + yc, ")") 
		print("(", -x + xc,",", y + yc, ")") 
		print("(", x + xc,",", -y + yc ,")") 
		print("(", -x + xc, ",", -y + yc, ")") 

		if (d1 < 0): 
			x += 1
			dx = dx + (2 * ry * ry)
			d1 = d1 + dx + (ry * ry)           # Decision parameter of region 1
		else: 
			x += 1
			y -= 1 
			dx = dx + (2 * ry * ry) 
			dy = dy - (2 * rx * rx)
			d1 = d1 + dx - dy + (ry * ry)

	# Decision parameter of region 2 
	d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
		((rx * rx) * ((y - 1) * (y - 1))) -
		(rx * rx * ry * ry))
 
	while (y >= 0):                             # For region 2
		print("(", x + xc, ",", y + yc, ")") 
		print("(", -x + xc, ",", y + yc, ")") 
		print("(", x + xc, ",", -y + yc, ")") 
		print("(", -x + xc, ",", -y + yc, ")") 

		if (d2 > 0): 
			y -= 1
			dy = dy - (2 * rx * rx) 
			d2 = d2 + (rx * rx) - dy 
		else: 
			x += 1
			y -= 1
			dx = dx + (2 * ry * ry) 
			dy = dy - (2 * rx * rx) 
			d2 = d2 + dx - dy + (rx * rx) 

 
if __name__ == '__main__':

    # To draw a ellipse of major and minor radius 15, 10 centred at (50, 50)
    midPointEllipse(10, 15, 50, 50)             

