

from PIL import Image
import json
import argparse

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(arg):
        return arg


def load_chars(path, pallet_idx=0, invert=False):
    with open(path, "rb") as file:
        chars = json.loads(file.read().decode("utf8"))[pallet_idx]
    chars = [c for c in chars]
    if invert:
        chars.reverse()

    return chars


def load_img(path, max_width=300):
    with Image.open(path) as img:
        img.load()

    # Convert to grayscale
    img = img.convert("L")

    width, height = img.size
    if width > max_width:
        ratio = width / height if width < height else height / width
        img = img.resize((max_width, int(max_width * ratio)), Image.Resampling.LANCZOS)

    return img


def colour_to_char(chars, val, max_val=255):
    val_percent = val / max_val
    return chars[int(len(chars) * val_percent)-1]


def img_to_str(img, chars, pixel_width=2, silent=False):
    out_string = ""
    width, height = img.size

    x, y = 0, -1

    for i, pixel in enumerate(tqdm(img.getdata()) if not silent else img.getdata()):
        x = i % width
        if x == 0:
            y += 1
            if y > 0:
                out_string += "\n"

        out_string += colour_to_char(chars, pixel) * pixel_width

    return out_string


def main():
    parser = argparse.ArgumentParser(
        prog="img2ascii",
        description="Convert an image into ASCII (or unicode) text"
    )
    parser.add_argument("image_path", help="Path to the image to convert")
    parser.add_argument("chars_path", help="Path to the chars file")
    parser.add_argument("-o", "--out_path", required=False, default=None, help="File to output to. If left blank, will output to console.")
    parser.add_argument("-w", "--width", type=int, required=False, default=300, help="Width to scale the image to. Default is 300px")
    parser.add_argument("-c", "--chars_idx", type=int, required=False, default=0, help="Index of the 'pallet' in the given chars json file")
    parser.add_argument("-i", "--invert", required=False, action="store_true", help="If included, image will be inverted")
    parser.add_argument("-p", "--pixel_width", required=False, default=2, type=int, help="How many characters to place per pixel. Should be adjusted based on font aspect ratio.")
    parser.add_argument("-s", "--silent", required=False, action="store_true", help="If included, only the output will be printed to the console")

    args = parser.parse_args()

    img = load_img(args.image_path, max_width=args.width)
    chars = load_chars(args.chars_path, args.chars_idx, invert=args.invert)

    out = img_to_str(img, chars, pixel_width=args.pixel_width, silent=args.silent)

    if args.out_path:
        with open(args.out_path, "wb") as file:
            file.write(out.encode("utf8"))
    else:
        print(out)


if __name__ == '__main__':
    main()