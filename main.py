import os
from PIL import Image
from distutils.dir_util import copy_tree

# todo: environmentふぁいるの個別設定


def main():
    path = "./result/textures"
    copy_tree("./textures", path)

    for pathname, dir_names, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".png"):
                execute(pathname + "/" + filename, 15)


def execute(file, threshold):
    img = Image.open(file).convert("RGBA")
    gray = Image.new("RGBA", img.size)
    px = img.load()
    counter = 0
    red = [80, 255]

    # ピクセルごとに条件合致するか調べ新しい画像として生成
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pixel = px[x, y]
            saturation = pixel[0]

            if red[0] <= pixel[0] <= red[1] and abs(pixel[1] - pixel[2]) <= threshold and pixel[1] <= pixel[0] and pixel[2] <= pixel[0]:
                gray.putpixel((x, y), pixel)
                counter += 1

            else:
                gray.putpixel((x, y), (saturation, saturation, saturation, pixel[3]))

    # if counter >= img.size[0] * img.size[1] / 5:
    #     img.save(file)
    #
    # else:
    #     for x in range(img.size[0]):
    #         for y in range(img.size[1]):
    #             pixel = px[x, y]
    #             saturation = pixel[0]
    #             gray.putpixel((x, y), (saturation, saturation, saturation, pixel[3]))

    gray.save(file)


if __name__ == "__main__":
    main()
