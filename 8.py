from PIL import Image
#Read image
im = Image.open('oxygen.png')

width, height = im.size
finHeight = height/2
img1 = im.crop(((finHeight-4), (finHeight-4), 608, (finHeight+4)))
img1.save("test.png")

im2 = Image.open('test.png')
p1 = 0

for i in range(304):
	r,g,b,a = im2.getpixel((p1,5))
	p1 = p1 + 2
	print (r, end=' ')