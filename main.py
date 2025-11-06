from PIL import Image, ImageFilter, ImageEnhance
from os import listdir

def flatten(xss):
  return [x for xs in xss for x in xs]

files = listdir("images")

for file in files:
  im = Image.open("images/" + file)
  blockBox = (109, 1965, 1175, 2283)
  im = im.crop(blockBox)

  source = im.split()

  R, G, B = 0, 1, 2

  mask = source[B].point(lambda i: i > 200 and 255)
  out = source[G].point(lambda i: 255)
  source[G].paste(out, None, mask)

  im = Image.merge(im.mode, source)

  colorEnchancer = ImageEnhance.Color(im)
  im = colorEnchancer.enhance(0)
  # sharpnessEnchancer = ImageEnhance.Sharpness(im)
  # im = sharpnessEnchancer.enhance(2)
  brightnessEnchancer = ImageEnhance.Brightness(im)
  im = brightnessEnchancer.enhance(1.05)
  contrastEnchancer = ImageEnhance.Contrast(im)
  im = contrastEnchancer.enhance(500)
  # im = im.filter(ImageFilter.FIND_EDGES)

  im.save("output/" + file)