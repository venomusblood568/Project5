import random
import string
from captcha.image import ImageCaptcha


# random.sample() function is used to jumble the characters in the generated random text. 
# The random.sample() function returns a new list containing unique elements randomly chosen from the input sequence.
def gen_random_text():
    length = random.randint(1,10)
    text = string.ascii_letters +string.ascii_lowercase+ string.ascii_uppercase + string.digits
    random_text=  ''.join(random.choice(text) for _ in range(length))
    jumbled_text = ''.join(random.sample(random_text, len(random_text)))  # Jumble the characters
    return jumbled_text

captcha_text = gen_random_text()

image = ImageCaptcha(width=280,height=90)

data = image.generate(captcha_text)

with open(captcha_text + ".png","wb") as f:
    f.write(data.read())
    print(f"CAPTCHA image '{captcha_text}.png' generated successfully.")



