from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from article.models import Article, Comment
from article.forms import CommentForm, ContactForm, EmailField
from shop.models import Product

def home(request):
    top_products = Product.objects.all()[:3]
    new_products = Product.objects.order_by('-id')[:8]
    latest_articles = Article.objects.order_by('-id')[:3]
    emailform = EmailField()
    if request.method == 'POST':
        emailform = EmailField(request.POST)
        if emailform.is_valid():
            emailform.save()
    context = {
        'emailform': emailform,
        'top_products': top_products,
        'new_products': new_products,
        'latest_articles': latest_articles
    }
    return render(request, 'index.html', context=context)

def article_page(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    emailform = EmailField()
    if request.method == 'POST':
        emailform = EmailField(request.POST)
        if emailform.is_valid():
            emailform.save()
    context = {
        'articles': articles,
        'page_obj': page_obj,
        'page_number': page_number,
        'emailform': emailform
    }
    return render(request, 'blog.html', context=context)

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = Comment.objects.all()
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.article = article
    emailform = EmailField()
    if request.method == 'POST':
        emailform = EmailField(request.POST)
        if emailform.is_valid():
            emailform.save()
    context = {
        'article': article,
        'form': form,
        'comments': comments,
        'emailform': emailform
    }
    return render(request, 'blog-details.html', context=context)

def contact_page(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    emailform = EmailField()
    if request.method == 'POST':
        emailform = EmailField(request.POST)
        if emailform.is_valid():
            emailform.save()
    context = {
        'form': form,
        'emailform': emailform
    }
    return render(request, 'contact.html', context=context)