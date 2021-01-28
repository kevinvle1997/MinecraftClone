from opensimplex import OpenSimplex

gen = OpenSimplex()

length = 20
width = 30

freq1 = 2
freq2 = 5
freq3 = 7


def noise(nx, ny):
    # Rescale from -1.0:+1.0 to 0.0:1.0
    return gen.noise2d(nx, ny) / 2.0 + 0.5


elevation = []
for y in range(length):
    elevation.append([0] * width)
    for x in range(width):
        nx = x / width - 0.5
        ny = y / length - 0.5
        elevation[y][x] = 1 * noise(nx * freq1, ny * freq1) + .33 * noise(nx * freq2, ny * freq2) + \
            .25 * noise(nx * freq3, ny * freq3)

print(elevation)
