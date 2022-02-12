from PIL import Image, ImageDraw

# DRAW FUNDO
im = Image.new('RGB', (800, 800), (128, 128, 128))
draw = ImageDraw.Draw(im)


WN = (200, 140)
ES = (580, 620)
outline_color = ('#43280D')

draw.ellipse([WN , ES], fill=('#EDA097'), outline=(outline_color), width=8)
im.save('parts/potato.png')
im.show()