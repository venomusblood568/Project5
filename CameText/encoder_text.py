# Import the numpy library with the alias "np."
import numpy as np 

# Import the PIL (Python Imaging Library) module for working with images.
import PIL.Image 

# Define the hidden text you want to encode in the image.
hidden_text = "to the moon"

# Open an image file named 'img_encoded.png' in read mode and assign it to the variable 'image.'
image = PIL.Image.open('img_encoded.png', "r")

# Get the width and height of the image.
width, height = image.size

# Convert the image data into a NumPy array and store it in the variable 'img_arr.'
img_arr = np.array(list(image.getdata()))

# Check if the image mode is 'P' (palette-based). If so, print a message and exit the program.
if image.mode == "P":
    print("img not supported")
    exit()

# Determine the number of color channels (3 for RGB, 4 for RGBA) based on the image mode.
channels = 4 if image.mode == "RGBA" else 3

# Calculate the number of pixels in the image.
pixels = img_arr.size // channels

# Define a stop indicator string.
Stop_indicator = "$PARADOX$"

# Calculate the length of the stop indicator string.
Stop_indicator_length = len(Stop_indicator)

# Add the stop indicator to the hidden text.
hidden_text += Stop_indicator

# Convert the hidden text to a binary string representation with 8 bits per character.
byte_message = ''.join(f"{ord(c):08b}" for c in hidden_text)

# Calculate the number of bits in the binary message.
bits = len(byte_message)

# Check if there is enough space in the image to encode the message.
if bits > pixels:
    print("Not enough space!")
else:
    # Initialize an index for iterating through the bits in the message.
    index = 0
    
    # Loop through the pixels and color channels of the image.
    for i in range(pixels):
        for j in range(0, 3):
            # Check if there are more bits to encode in the message.
            if index < bits:
                # Modify the least significant bit of the color channel with a bit from the message.
                img_arr[i][j] = int(bin(img_arr[i][j])[2:-1] + byte_message[index], 2)
                index += 1

# Reshape the modified image array to its original dimensions.
img_arr = img_arr.reshape((height, width, channels))

# Create a new image from the modified image array.
result = PIL.Image.fromarray(img_arr.astype("uint8"), image.mode)

# Save the encoded image as 'encoded.png.'
result.save("encoded.png")

# Print a message indicating that encoding was successful.
print("encoded successful")
