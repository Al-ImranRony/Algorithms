'''
Graphics Assignment 01
Bresenham's line generation algorithm 

Assumptions:- Line is drawn from left to right
            - In coordinates must have x1 < x2 and y1 < y2
            - Slope must be between 0 and 1
            - Drawing the line from lower left to upper right  
'''

def bresenhamLine(x1, y1, x2, y2):
    d_new = 2 * (y2 - y1)
    slopeErrNew = d_new - (x2 - x1)
    y = y1

    for x in range(x1, x2+1):
        print("(", x, ',', y, ")\n")

        # slopeErrNew += d_new
        if (slopeErrNew >= 0):
            slopeErrNew += d_new
            y += 1
            slopeErrNew -= (2 * (x2 - x1))


if __name__ == '__main__':
    x1, y1, x2, y2 = 3, 2, 15, 5
    bresenhamLine(x1, y1, x2, y2)

