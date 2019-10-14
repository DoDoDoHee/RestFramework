from django.db import models
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    # author가 없으면 default로 1을 줘라
    # on_delete는 저자가 없어지면 글도 없애라 그런개념
    # 회원이 탈퇴하면 그 글도 함께 삭제할건가 하는 개념
    title = models.TextField(max_length=100)
    body = models.TextField()

class BlogPic(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    myimage = models.ImageField(upload_to='images', default="null")
    desc = models.CharField(max_length=100)
# upload_to 내가 어디에 upload를 할건지 경로지정해줌

class BlogFile(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    myfile = models.FileField(upload_to='files', blank=False, null=False)
    desc = models.CharField(max_length=100)
