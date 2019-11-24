# Create an image file (png) from code.
# hint: use Pillow

# from PIL import Image, ImageDraw
# img = Image.new(mode, size, color)
# img.save(filename)

# from PIL import Image
# img = Image.new('RGB', (60, 30), color = 'red')
# img.save('pil_red.png')

# from PIL import Image, ImageDraw
#
# img = Image.new('RGB', (100, 30), color = (73, 109, 137))
# d = ImageDraw.Draw(img)
# d.text((10,10), "Hello World", fill=(255,255,0))
# img.save('pil_text.png')

from PIL import Image, ImageDraw
Myimage = Image.new('RGB', (220,60), color='black')
t = ImageDraw.Draw(Myimage)
t.text((10,10), "Great success !!!")
Myimage.save("Image.png")
