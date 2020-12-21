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
    nimg = Image.new(
        "RGB", (img.width * n, img.height * n), "black"
    )  # create a new black image
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


def test_transform():
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
