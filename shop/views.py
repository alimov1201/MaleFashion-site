from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from shop.models import Product, Category
from article.forms import EmailField

def shop(request):
    search = request.GET.get('search')
    category = request.GET.get('category')
    if category:
        products = Product.objects.filter(category=category)
    elif search:
        products = Product.objects.filter(name__icontains=search)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    all_categories = Category.objects.all()
    emailform = EmailField()
    if request.method == 'POST':
        emailform = EmailField(request.POST)
        if emailform.is_valid():
            emailform.save()
    context = {
        'page_obj': page_obj,
        'page_number': page_number,
        'category': category,
        'all_categories': all_categories,
        'emailform': emailform,
        'search': search
    }
    return render(request, 'shop.html', context=context)

def shop_detail(request, id):
    product = get_object_or_404(Product, id=id)
    emailform = EmailField()
    if request.method == 'POST':
        emailform = EmailField(request.POST)
        if emailform.is_valid():
            emailform.save()
    context = {
        'product': product,
        'emailform': emailform
    }
    return render(request, 'shop-details.html', context=context)
