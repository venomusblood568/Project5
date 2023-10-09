from captcha.image import ImageCaptcha

width = input("enter the width of the img: ")
height = input("enter the height of the img: ")
captcha_text = input("enter the smaple text: ")
png_name = input("enter the name for img: ")

image = ImageCaptcha(width=int(width),height=int(height))

data = image.generate(captcha_text)

with open(png_name + ".png","wb") as f:
    f.write(data.read())
    print(f"CAPTCHA image '{png_name}.png' generated successfully.")
