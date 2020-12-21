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


def xtest_rm():
    path = "./images/LutherBellPic.jpg"
    img = rm_red(path)
    img.show()


if __name__ == "__main__":
    path = "./images/LutherBellPic.jpg"
    img = rm_red(path)
    img.show()

