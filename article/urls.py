from django.urls import path
from article.views import home, article_detail, contact_page, article_page

urlpatterns = [
    path('', home, name='home'),
    path('blog/', article_page, name='blog'),
    path('blog_detail/<int:id>/', article_detail, name='article_detail'),
    path('contact/', contact_page, name='contact')
]