from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post

# Create your views here.
def helloBlog(request):
  # return HttpResponse('Blog')
  lista = ['Django', 'Python', 'Git', 'Html', 'Banco de Dados', 'Linux', 'Nginx', 'Uwsgi', 'Systemctl']
  postsList = Post.objects.all()
  data = {'name': 'Lucas Aquino', 'listaTecnologias' : lista, 'posts': postsList}
  
  return render(request, 'index.html', data)
