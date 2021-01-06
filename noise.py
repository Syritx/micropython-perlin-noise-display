import math

SEED = 0


class vector2:
    x = 0
    y = 0

    def __init__(self, x, y):
	self.x = x
	self.y = y


def seed(s):
    global SEED
    SEED = s

def interpolate(a, b, w):
    return pow(w, 2) * (3 - 2 * w) * (b-a) + a

def generate_gradient(ix, iy):
    rand = SEED * math.sin(ix*21942 + iy*171324 + 8912) * math.cos(ix*23157 * iy * 217832 + 6758)
    gradient = vector2(math.sin(rand), math.cos(rand))
    #print(SEED)
    return gradient

def dot_product(ix, iy, x, y):
    gradient = generate_gradient(ix, iy)
    
    xDist = x - float(ix)
    yDist = y - float(iy)

    return (xDist * gradient.x + yDist * gradient.y)

def noise(x, y):
    x0 = int(x)
    x1 = x0 + 1

    y0 = int(y)
    y1 = y0 + 1

    sx = x - float(x0)
    sy = y - float(y0)

    d1 = dot_product(x0, y0, x, y)
    d2 = dot_product(x1, y0, x, y)
    int1 = interpolate(d1, d2, sx)

    d3 = dot_product(x0, y1, x, y)
    d4 = dot_product(x1, y1, x, y)
    int2 = interpolate(d3, d4, sx)

    val = interpolate(int1, int2, sy)
    return val
