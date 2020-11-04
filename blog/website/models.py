from django.db import models

# Create your models here.
class Categories(models.TextChoices):
  TECH = 'TC', 'Tecnologia'
  CR = 'CR', 'Curiosidades'
  GR = 'GR', 'Geral'

class Post(models.Model):
  title = models.CharField(max_length=100)
  subTitle = models.CharField(max_length=200)
  content = models.TextField()
  categories = models.CharField(max_length = 2, choices = Categories.choices, default = Categories.GR)
  deleted = models.BooleanField(default=False)
  imagem = models.ImageField(upload_to = 'posts', null=True, blank=True) #define a pasta dentro do MEDIA_ROOT onde imagens serão salvas, setando como não obrigatório

  def __str__(self):
    return self.title

  def fullName(self):
    return self.title + self.subTitle

  def getCategoryLabel(self):
    return self.get_categories_display()

  fullName.admin_order_field = 'title'

class Contact(models.Model):
  name = models.CharField(max_length=150)
  email = models.EmailField()
  message = models.TextField()

  def __str__(self):
    return self.name