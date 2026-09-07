from PIL import Image

def convert(code):
    if code == "R":
        return (237, 28, 36)
    elif code == "B":
        return (0, 0, 0)
    elif code == "Y":
        return (255, 242, 0)
    else:
        return (255, 255, 255)

input_text_file = open("awesome_picture.txt", "r")
lines = input_text_file.readlines()
input_text_file.close()

h = len(lines)
w = len(lines[0].split())

image = Image.new(
    mode="RGB",
    size=(w, h),
    color=(0, 0, 0)
)

print("Height:", h)
print("Width:", w)
print("\nImage using R, B and Y:\n")

for y in range(h):
    pixels = lines[y].split()
    print(" ".join(pixels))

    for x in range(w):
        pixel = pixels[x]
        image.putpixel((x, y), convert(pixel))
image.save("smiley2.png")
print("\nThe new image was saved as smiley2.png")