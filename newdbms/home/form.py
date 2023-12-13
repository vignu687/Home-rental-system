from django import forms 
from captcha.fields import CaptchaField

class Captchaform(forms.Form):
    captcha=CaptchaField()
