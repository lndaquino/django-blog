from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def helloBlog(request):
  # return HttpResponse('Blog')
  lista = ['Django', 'Python', 'Git', 'Html', 'Banco de Dados', 'Linux', 'Nginx', 'Uwsgi', 'Systemctl']
  data = {'name': 'Lucas Aquino', 'listaTecnologias' : lista}
  return render(request, 'index.html', data)
