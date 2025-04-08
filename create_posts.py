from django.contrib.auth.models import User
from blog.models import Post
import lorem

user = User.objects.get(username = 'iraqez')

def lorPost(x, y):
    for i in range(x, y):
        lor = lorem.get_paragraph(count=3)
        Post(title='Тестовий пост №'+str(i), slug='post-from-shell'+str(i), body=lor, author=user, status='PB').save()

if __name__ == '__main__':
    lorPost(1, 40)