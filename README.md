# image_to_ascii
A simple CLI program for converting images into text. While ASCII is in the name, it works with any unicode characters, and the specific characters used can easily be customised using the `chars.json` file.

## Usage
```
usage: img_to_ascii.py [-h] [-o OUT_PATH] [-w WIDTH] [-c CHARS_IDX] [-i] [-p PIXEL_WIDTH] [-s] image_path chars_path

Convert an image into ASCII (or unicode) text

positional arguments:
  image_path            Path to the image to convert
  chars_path            Path to the chars file

options:
  -h, --help            show this help message and exit
  -o OUT_PATH, --out_path OUT_PATH
                        File to output to. If left blank, will output to console.
  -w WIDTH, --width WIDTH
                        Width to scale the image to. Default is 300px
  -c CHARS_IDX, --chars_idx CHARS_IDX
                        Index of the 'pallet' in the given chars json file
  -i, --invert          If included, image will be inverted
  -p PIXEL_WIDTH, --pixel_width PIXEL_WIDTH
                        How many characters to place per pixel. Should be adjusted based on font aspect ratio.
  -s, --silent          If included, only the output will be printed to the console

```

### Example
The following command will convert `example/ubuntu.png` into text, using the pallet at index 2 of `chars.json`. The image will be scaled to a width of 125px, and there will be 2 characters per pixel. The output will be saved to `examples/ubuntu_out.txt`.

`$ python image_to_ascii.py examples/ubuntu.png chars.json -o examples/ubuntu_out.txt -c 2 -w 125 -p 2`

## Chars file
Colour "pallets" are defined in the chars file. An example chars file is included in `chars.json`. chars files should be json files that contain a single array of strings. Each character in the string will be used as a shade of gray to create the image, meaning the darkest pixels will be represented with the first character, and the brightest pixels will be represented with the last character.

## Attribution
The images used in `examples/` are not my own. Attribution for these images is included below, as needed.

### `tux.png` - CC0
Attribution: lewing@isc.tamu.edu Larry Ewing and The GIMP

