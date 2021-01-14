'''
Graphics Assignment 03
Bresenham's circle generation algorithm
''' 

from PIL import Image, ImageDraw


# def drawCircle(xc, yc, x, y):
#     putpixel(xc+x, yc+y, RED)
#     putpixel(xc-x, yc+y, RED) 
#     putpixel(xc+x, yc-y, RED) 
#     putpixel(xc-x, yc-y, RED) 
#     putpixel(xc+y, yc+x, RED) 
#     putpixel(xc-y, yc+x, RED) 
#     putpixel(xc+y, yc-x, RED) 
#     putpixel(xc-y, yc-x, RED)


def bresenhamCircle(radius):
    x, y, d = 0, radius, 3-(2 * radius)
    points = set()

    while (y >= x):
        points.add((x,-y))          # first quarter first octant        
        points.add((y,-x))          # first quarter 2nd octant        
        points.add((y,x))           # second quarter 3rd octant        
        points.add((x,y))           # second quarter 4.octant        
        points.add((-x,y))          # third quarter 5.octant    
        points.add((-y,x))          # third quarter 6.octant        
        points.add((-y,-x))         # fourth quarter 7.octant        
        points.add((-x,-y))         # fourth quarter 8.octant

        if (d < 0):
            d = d + (4 * x) + 6
        else:
            d = d + (4 * (x-y)) + 10
            y -= 1
        x += 1
    return points


size, radius = 200, 50
circle_graph = Image.new("RGB", (size, size), (0,0,0))
draw = ImageDraw.Draw(circle_graph)

points = bresenhamCircle(radius)
print(points)
for point in points:
    draw.point((size/2+point[0], size/2+point[1]), "RED")

circle_graph.show()
