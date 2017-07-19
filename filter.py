from PIL import Image

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

choice = input("Which image would you like: 1)cute animal, 2) city skyline, or 3) pretty flower?")
if choice == "2":
    my_image = Image.open("nyc.jpg")
elif choice == "1":
    my_image = Image.open("gr.jpg")
elif choice == "3":
    my_image = Image.open("flower1.jpg")
else:
    print("Incorrect input")

image_list = my_image.getdata()
image_list = list(image_list)
recolored = []

for pixel in image_list:
    x = (pixel[0] + pixel[1] + pixel[2])
    if (x < 182):
        recolored.append(darkBlue)
    elif (x == 182):
        recolored.append(red)
    elif (182 < x < 364):
        recolored.append(red)
    elif (x == 364):
        recolored.append(lightBlue)
    elif (364 < x < 546):
        recolored.append(lightBlue)
    elif (x == 546):
        recolored.append(yellow)
    elif (x > 546):
        recolored.append(yellow)


new_image = Image.new("RGB", my_image.size)
new_image.putdata(recolored)
new_image.show()
new_image.save("recolored.jpg", "jpeg")
