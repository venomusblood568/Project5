# these are the last bit of the image so we are just adding some text here so this line will be same.
end_hex = b"\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

#hori_hide.png is the traget image  and the ab is the mode 
with open("hori_hide.png",'ab') as f:
    f.write(b"hey darling!") #here is the message
    print("successful") # just for confirmation a text is provided

#ab mode opens a file for appending in binary mode.
#The a stands for append, and the b stands for binary.