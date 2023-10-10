#pip install captcha.audio 
from captcha.audio import AudioCaptcha

def generate_audio_captcha(captch_text):
    audio = AudioCaptcha()
    audio_data = audio.generate(captch_text)

    audio_file = "audio"+captch_text+".wav"
    with open(audio_file,"wb") as f:
        f.write(audio_data)
        print(f"Audio file '{audio_file}' was built successfully.")

captcha_text = input("enter the number for captcha: ")
generate_audio_captcha(captcha_text)