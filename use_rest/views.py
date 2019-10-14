from django.shortcuts import render
from .models import Blog, BlogPic, BlogFile
from .serializer import BlogSerializer, BlogPicSerializer, BlogFileSerializer
# viewset을 사용한다고 명시해주자! 
from rest_framework import viewsets

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('id') # pagenation을 사용하기 위해 정렬해줌, 먼저 글작성된건 첫번째로되고 
    serializer_class = BlogSerializer

    def perform_create(self, serializer): # create가 동작할때, save할 때 author를 같이 넘겨줘라
        serializer.save(author=self.request.user) # self는 instance
    
    def get_queryset(self):
        qs = super().get_queryset() # 우리 모델에 있는 모든 data를 가져온다

        if self.request.user.is_authenticated: # 로그인이 되어 있다면
            qs = qs.filter(author=self.request.user) # 저자가 같은 사람만 filter해서 보여주자, 내글 보기 기능
        else:
            qs = qs.none()
        return qs

    
class BlogPicViewSet(viewsets.ModelViewSet):
    queryset = BlogPic.objects.all().order_by('id')
    serializer_class = BlogPicSerializer

class BlogFileViewSet(viewsets.ModelViewSet):
    queryset = BlogFile.objects.all().order_by('id')
    serializer_class = BlogFileSerializer