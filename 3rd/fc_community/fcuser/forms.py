from django import forms
from django.contrib.auth.hashers import check_password

from .models import Fcuser


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required' : '아이디를 입력하셈'
        }, max_length=32, label="사용자 이름")
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력하셈'
        },
        widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist:
                self.add_error('username', '아이디가 없습니다')

            if not check_password(password, fcuser.password):
                self.add_error('password', 'wrong password')
            else:
                self.user_id = fcuser.id
