from PIL import Image

img = Image.open("DSC04893.JPG")
data = img.getdata()

for x in data:
	print(x)