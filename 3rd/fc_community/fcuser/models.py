from django.db import models

# Create your models here.

class Fcuser(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name='사용자명')
    useremail = models.EmailField(max_length=128,
                                  verbose_name='사용자이메일')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                verbose_name='등록시간')

    # 문자열을 반환할 때 어떻게 봔환할 지 변경 '__str__()'
    def __str__(self):
        return self.username

    # 모델 취급 방법 변경
    class Meta:
        # DB 테이블 이름 변경
        db_table = 'fastcampus_Fcuser'
        # admin페이지 모델 표기 방법 변경
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자' # 복수형 표시