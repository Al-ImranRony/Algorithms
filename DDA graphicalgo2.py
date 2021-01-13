'''
Graphics algorithm 02
Digital Differential Analyser (DDA) line drawing algorithm 
'''

def round(p):
    return int(p + 0.5)

def drawDDA(x1, y1, x2, y2):
    x, y = x1, y1
    if (x2-x1) > (y2-y1):
        length = x2-x1
    else:
        length = y2-y1  

    dx = (x2-x1) / float(length)
    dy = (y2-y1) / float(length)

    print(f'({round(x)}, {round(y)})')

    for i in range(length):
        x += dx
        y += dy
        print(f'({round(x)}, {round(y)})')


if __name__ == "__main__":
    x1, y1, x2, y2 = 2, 5, 10, 20
    drawDDA(x1, y1, x2, y2)