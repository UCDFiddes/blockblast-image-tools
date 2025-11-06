from PIL import Image
im = Image.open("images/test_1.png")

blockBox = (0, 1965, 1284, 2283)
im = im.crop(blockBox)

im.save("output.png")