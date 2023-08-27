# these are the last bit of the image so we are just adding some text here so this line will be same.
end_hex = b"\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

# hori_hide.png is the target img and rb is the mode 
with open('hori_hide.png','rb') as f:
    content = f.read()
    offset = content.index(end_hex)
    f.seek(offset+len(end_hex))
    print(f.read())
    print("Message reveal successful")
#The rb mode opens a file in binary mode for reading. This is the default mode for opening files in Python.

