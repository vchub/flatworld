from PIL import Image


def rm_red(path) -> Image:
    """Remove red from every pixel"""
    img = Image.open(path)
    h, w = img.size
    # nimg = Image.new("RGB", (h, w), "black")  # create a new black image
    ps = img.load()
    for i in range(h):
        for j in range(w):
            r, g, b = ps[i, j]
            ps[i, j] = (0, g, b)

    return img


def grey_scale(path) -> Image:
    """Remove red from every pixel"""
    img = Image.open(path)
    h, w = img.size
    # nimg = Image.new("RGB", (h, w), "black")  # create a new black image
    ps = img.load()
    for i in range(h):
        for j in range(w):
            r, g, b = ps[i, j]
            a = (r+g+b)//3
            ps[i, j] = (a, a, a)

    return img


def black_white(path) -> Image:
    """Remove red from every pixel"""
    img = Image.open(path)
    h, w = img.size
    # nimg = Image.new("RGB", (h, w), "black")  # create a new black image
    ps = img.load()
    for i in range(h):
        for j in range(w):
            r, g, b = ps[i, j]
            a = (r+g+b)//3
            if a < 120:
                a = 0
            else:
                a = 255
            ps[i, j] = (a, a, a)

    return img


def mult_2(scale: int, img: Image) -> Image:
    """scale pict in n times"""
    nimg = Image.new("RGB", (img.width*scale, img.height*scale),
                     "black")  # create a new black image
    ps = img.load()
    ps1 = nimg.load()
    for x in range(img.width):
        for y in range(img.height):
            x1, y1 = x*scale, y*scale
            for i in range(scale):
                for j in range(scale):
                    ps1[x1+i, y1+j] = ps[x, y]

    return nimg


# print table 4x4 of 1
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1

def transform(fn: callable, img: Image):
    ps = img.load()
    for x in range(img.width):
        for y in range(img.height):
            # make transformation
            ps[x, y] = fn(ps[x, y])


# p = (100, 200, 50)
# p[0]
# r,g,b = (100, 200, 50)
# print(r,g,b)
if __name__ == "__main__":
    path = "./images/LutherBellPic.jpg"
    img = Image.open(path)

    nimg = mult_2(4, img)
    nimg.show()

    def id(p):
        return p

    def remove_red(p):
        r, g, b = p
        return (0, g, b)

    def grey_sc(p):
        r, g, b = p
        # v = (r+g+b)//3
        v = sum(p)//3
        return (v, v, v)

    def bw(p):
        v = sum(p)//3
        if v < 100:
            v = 0
        else:
            v = 255
        return (v, v, v)

    def sepia(p):
        R, G, B = p
        newR = int(R * 0.393 + G * 0.769 + B * 0.189)
        newG = int(R * 0.349 + G * 0.686 + B * 0.168)
        newB = int(R * 0.272 + G * 0.534 + B * 0.131)
        return (newR, newG, newB)

    # transform(sepia,img)

    #img = rm_red(path)
    #img = grey_scale(path)
    #img = black_white(path)
    # img = mult_2(path)
    # img.show()


def test_rm():
    path = "./images/LutherBellPic.jpg"
    img = rm_red(path)
    img.show()



# git config --global user.name "nnng"
# git config --global user.email "nnng@gmail.com"

