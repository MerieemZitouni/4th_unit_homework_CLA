from PIL import Image
img = Image.open('cat.jpg')
img.show()
img = img.transpose(Image.TRANSPOSE)
img.show()