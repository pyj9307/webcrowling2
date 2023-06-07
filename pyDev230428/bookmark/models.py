from django.db import models

# Create your models here.
class Bookmark(models.Model):
    # 문자필드, 최대문자열 길이 100, 공백허용, null허용
    title=models.CharField(max_length=100,blank=True,null=True)
    url=models.URLField('url',unique=True)
    
    # def __init__(self,title):
    #     self.title=title
    #     #생성자
    
    def __str__(self): # def __str__(self) : toString() 함수와 같음
        return self.title