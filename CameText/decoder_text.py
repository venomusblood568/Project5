# Import the numpy library with the alias "np."
import numpy as np

# Import the PIL (Python Imaging Library) module for working with images.
import PIL.Image  

# Open an image file named "encoded.png" in read mode and assign it to the variable "image."
image = PIL.Image.open("encoded.png", "r")

# Convert the image data into a NumPy array and store it in the variable "img_arr."
img_arr = np.array(list(image.getdata()))

# Determine the number of color channels (3 for RGB, 4 for RGBA) based on the image mode.
#RGBA is a color model that represents colors with Red, Green, Blue values (for color) and an Alpha value (for transparency).
channels = 4 if image.mode == "RGBA" else 3

# Calculate the number of pixels in the image.
pixels = img_arr.size // channels

# Extract the least significant bit (LSB) from each color channel of each pixel and store it as binary strings.
secret_bits = [bin(img_arr[i][j])[-1] for i in range(pixels) for j in range(0, 3)]

# Join the binary strings into one continuous binary string.
secret_bits = ''.join(secret_bits)

# Split the continuous binary string into 8-bit chunks.
secret_bits = [secret_bits[i:i+8] for i in range(0, len(secret_bits), 8)]

#this line is for priting every bit of img in pair of 8s
#print(secret_bits)


# Convert each 8-bit binary chunk into a character and form a list of characters representing the secret message.
secret_message = [chr(int(secret_bits[i], 2)) for i in range(len(secret_bits))]

# Join the list of characters into a single string, which is the decoded secret message.
secret_message = ''.join(secret_message)

# Define a stop indicator string.keep the stop_indicator as same...

Stop_indicator = "$PARADOX$"

# Check if the stop indicator is found within the secret message.
if Stop_indicator in secret_message:
    # If found, print the part of the secret message before the stop indicator.
    print(secret_message[:secret_message.index(Stop_indicator)])
else:
    # If not found, print "No Message found!"
    print("No Message found!")


