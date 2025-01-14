from PIL import Image

path = input("Enter the image location: ")

try:
    img = Image.open(path)
except FileNotFoundError:
    print("No such file was found")
    exit(1)
except Exception as e:
    print(e, " error has occured")
    exit(2)


invert = img.convert('RGB')

pixel = invert.load()


for x in range(img.width):
    for y in range(img.height):
        r, g, b = pixel[x, y]
        pixel[x, y] = (255-r, 255-g, 255-b)


invert.save('invert.png')

print("The Inverted copy of image has been successfully saved to same directory, named as 'invert.png'")