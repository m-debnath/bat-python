def make_pi():
    """Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}."""
    spi = str(math.pi)
    list = [int(spi[0]), int(spi[2]), int(spi[3])]
    return list