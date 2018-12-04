from django import forms
from captcha.fields import CaptchaField


class RegisterForm(forms.Form):
    name = forms.CharField(label="请输入用户名", required=True, min_length=5, max_length=10)
    pwd = forms.CharField(label="请输入密码", required=True, min_length=4, max_length=8)
    email = forms.EmailField(label="请输入电子信箱", required=True)
    captcha = CaptchaField(label="请输入验证码", error_messages={"invalid": u"验证码错误"})


class UploadForms(forms.Form):
    user = forms.CharField(label="请输入用户名", required=True)
    file = forms.FileField(label="选择上传的文件", required=True)