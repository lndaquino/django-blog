from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post, Contact

# Create your views here.
def helloBlog(request):
  # return HttpResponse('Blog')
  lista = ['Django', 'Python', 'Git', 'Html', 'Banco de Dados', 'Linux', 'Nginx', 'Uwsgi', 'Systemctl']
  postsList = Post.objects.filter(deleted=True)
  data = {'name': 'Lucas Aquino', 'listaTecnologias' : lista, 'posts': postsList}
  
  return render(request, 'index.html', data)


def postDetail(request, id):
  post = Post.objects.get(id=id)
  return render(request, 'postDetail.html', {'post': post})

def saveForm(request):
  print(request.POST)
  name = request.POST['name']
  Contact.objects.create(
    name = name,
    email = request.POST['email'],
    message = request.POST['message'],
  )
  return render(request, 'contactSucess.html', {'nameContact': name})
