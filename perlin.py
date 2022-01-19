from opensimplex import OpenSimplex

gen = OpenSimplex()

length = 20
width = 20

freq1 = 15
freq2 = 10
freq3 = 20


def noise(nx, ny):
    # Rescale from -1.0:+1.0 to 0.0:1.0
    return gen.noise2(nx / 10, ny / 10) / 3.0 + 0.5 * 10

def lerp(t, a, b):
    """Linear interpolation between a and b, given a fraction t."""
    return a + t * (b - a)

elevation = []
for y in range(length):
    elevation.append([0] * width)
    for x in range(width):
        nx = x / width - 0.5
        ny = y / length - 0.5
        elevation[y][x] = lerp(noise(nx * freq1, ny * freq1), noise(nx * freq2, ny * freq2), noise(nx * freq3, ny * freq3))
