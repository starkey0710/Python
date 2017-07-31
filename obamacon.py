from PIL import Image

# RGB values for recoloring.
lightYellow = (249, 237, 162)
purple = (226, 162, 249)
lightBlue = (164, 237, 252)
randomColor = (249, 163, 162)


# Import image.
my_image = Image.open("space-needle.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

length = len(image_list)

for count in range(length):
    image_list[count]
    rgb_list = image_list[count]
    rgb_sum = rgb_list[0] + rgb_list[1] + rgb_list[2]
    if rgb_sum < 182:
        pixel = lightYellow
        recolored.append(pixel)
        # color it dark blue
    elif rgb_sum >= 182 and rgb_sum < 364:
        pixel = purple
        recolored.append(pixel)
        # color it red
    elif rgb_sum >= 364 and rgb_sum < 546:
        pixel = lightBlue
        recolored.append(pixel)
        # color it light blue
    else:
        pixel = randomColor
        recolored.append(pixel)
        # color it yellow

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.



# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
