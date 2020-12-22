from PIL import Image


def transform_image(fn: callable, img: Image):
    for x in range(img.width):
        for y in range(img.height):
            img.putpixel((x, y), fn(img.getpixel((x, y))))


def transform_file(fn: callable, path) -> Image:
    """transform image of the file
    fn: (int, int, int) -> (int, int, int)
    """
    img = Image.open(path)
    transform_image(fn, img)

    # w, h = img.size
    # ps = img.load()
    # for i in range(w):
    #     for j in range(h):
    #         img[i, j] = fn(img[i, j])

    return img


def scale(n: int, img: Image):
    """scale image by n """
    w, h = img.size
    ps = img.load()
    # create a new black image
    nimg = Image.new("RGB", (img.width * n, img.height * n), "black")
    nps = nimg.load()
    for i in range(w):
        for j in range(h):
            p = ps[i, j]
            for r in range(n):
                for c in range(n):
                    nps[i * n + r, j * n + c] = p

    return nimg


def smooth(c: int, img: Image):
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = 0, 0, 0
            cnt = 0
            for k in range(-c, c + 1):
                for l in range(-c, c + 1):
                    xx = x + k
                    yy = y + l
                    if xx < 0 or xx >= img.width or yy < 0 or yy >= img.height:
                        continue
                    r1, g1, b1 = img.getpixel((xx, yy))
                    r += r1
                    g += g1
                    b += b1
                    cnt += 1

            img.putpixel((x, y), (r // cnt, g // cnt, b // cnt))


def xtest_transform():
    path = "./images/LutherBellPic.jpg"
    img = Image.open(path)

    def invert(p: tuple) -> tuple:
        return tuple(255 - x for x in p)

    def id(x):
        return x

    def sepia(p: tuple) -> tuple:
        r, g, b = p
        r = int(r * 0.393 + g * 0.769 + b * 0.189)
        g = int(r * 0.349 + g * 0.686 + b * 0.168)
        b = int(r * 0.272 + g * 0.534 + b * 0.131)
        return (r, g, b)

    # transform_image(sepia, img)
    img = scale(4, img)
    # smooth(2, img)

    img.show()


def xtest_matrix():
    # создает matrix из нулей заданной ширины и высоты
    def zero_matrix(width, height) -> list:
        """creates matrix of zeroes, of given width and height"""
        NotImplemented
        return [[0] * width for _ in range(height)]

    assert zero_matrix(1, 1) == [[0]]
    assert zero_matrix(2, 3) == [
        [0, 0],
        [0, 0],
        [0, 0],
    ]

    # check assignment
    a = zero_matrix(3, 3)
    a[0][0] = 1
    assert a[0][0] == 1
    assert a[1][0] != 1
    assert a[0][1] != 1

    # делает копию matrix заданной ширины и высоты
    def copy(a: list, width: int, height: int) -> list:
        b = zero_matrix(width, height)
        for i in range(width):
            for j in range(height):
                b[j][i] = a[j][i]

        return b

    a = zero_matrix(2, 3)
    a[0][0] = 1
    b = copy(a, width=2, height=3)
    b[1][0] = 2
    assert a[0][0] == 1
    assert b[0][0] == 1
    assert b[1][0] == 2
    assert a[1][0] == 0

    # увеличивает matrix заданной ширины и высоты в factor раз
    def scale(a: list, width: int, height: int, factor: int) -> list:
        b = zero_matrix(width * factor, height * factor)
        for i in range(height):
            for j in range(width):
                for k in range(factor):
                    for l in range(factor):
                        b[i * factor + k][j * factor + l] = a[i][j]
        return b

    a = [[1]]
    b = scale(a, 1, 1, 1)
    assert b == [[1]]

    b = scale(a, 1, 1, 3)
    assert b == [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]

    a = [[1, 2, 3], [4, 5, 6]]
    b = scale(a, 3, 2, 3)
    # print(b)
    assert len(b) == 2 * 3
    assert len(b[0]) == 3 * 3
    assert b[1 * 3][2 * 3] == 6


#

#
