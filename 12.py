from PIL import Image
i = Image.open("cave.jpg").convert('RGB')

pixels = i.load()
width, height = i.size

all_pixels = []
odd = 1
for y in range(height):
    for x in range(width):
        if odd:
            all_pixels.append(i.getpixel((x, y)))
            odd=0
        else:
            odd=1
im2 = Image.new("RGB", i.size )
im2.putdata(all_pixels)
im2.save('out.png')






















# import requests
# import re

# BaseUrl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
# oldExt = "72758"
# pattern = re.compile("next nothing is (.+)")

# def getData(ext):
#     catUrl = BaseUrl+ext
#     webp = requests.get(catUrl).text
#     pageData = str(webp)
#     print (pageData)
#     test = pattern.search(pageData)
#     # if pageData == "Yes. Divide by two and keep going.":
#     #     return "8022"
#     if test.group(1):
#         return test.group(1)
#     else:
#         print (pageData)

# for i in range(10000):
#     newExt = getData(oldExt)
#     oldExt = newExt
