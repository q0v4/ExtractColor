from PIL import Image
import sys


def grayscale(file, mode="hsv"):
    img = Image.open(file).convert("RGBA")
    gray = Image.new("RGBA", img.size)
    px_map = img.load()

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pixel = px_map[x, y]
            saturation = 0

            rgb = list(pixel)
            del rgb[3]

            if mode == "hsv":
                saturation = max(rgb)
            elif mode == "hls":
                saturation = min(rgb)
            else:
                print("modeの値が不正です。以下の値を指定してください:[hsv|hls]")
                sys.exit()

            gray.putpixel((x, y), (saturation, saturation, saturation, pixel[3]))

    gray.save(file)


def extractColor(file, color_mode, color_range, threshold, mode="hsv"):
    img = Image.open(file).convert("RGBA")
    gray = Image.new("RGBA", img.size)
    px_map = img.load()
    count = 0   # 着色数をカウント

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pixel = px_map[x, y]
            r, g, b = [0, 0], [0, 0], [0, 0]

            # 抜き出したい色を選択
            index = [i for i in range(3)]
            pick = index.pop(color_mode)

            # 条件合致したピクセルのみそのまま描画、それ以外をグレースケールに
            if color_range[0] <= pixel[pick] <= color_range[1] \
                    and abs(pixel[index[0]] - pixel[index[1]]) <= threshold \
                    and pixel[index[0]] <= pixel[pick] \
                    and pixel[index[1]] <= pixel[pick]:
                gray.putpixel((x, y), pixel)
                count += 1

            else:
                rgb = list(pixel)
                del rgb[3]

                if mode == "hsv":
                    saturation = max(rgb)
                elif mode == "hls":
                    saturation = min(rgb)
                else:
                    print("modeの値が不正です。以下の値を指定してください:[hsv|hls]")
                    sys.exit()

                gray.putpixel((x, y), (saturation, saturation, saturation, pixel[3]))

    if count <= img.size[0] * img.size[1] / 3:
        grayscale(file)

    else:
        gray.save(file)