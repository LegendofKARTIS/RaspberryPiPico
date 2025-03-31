from PIL import Image

def convert_to_rgb565(image_path, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    img = img.resize((320, 240))

    with open(output_path, "wb") as f:
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = img.getpixel((x, y))
                rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
                f.write(rgb565.to_bytes(2, "big"))
                print('Done')

convert_to_rgb565("D:\\Your Path of Image need to be converted\\hello.png", "C:\\Users\\Desktop\\The path of image that to be stored after conversion is completed\\hello.rgb")
