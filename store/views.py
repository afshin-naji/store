from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q
from django.core.paginator import Paginator
from comment.forms import CommentForm


def categories(request):
    return{
        'categories': Category.objects.all()
    }


def all_products(request):
    page = request.GET.get('page', 1)

    search_product = request.GET.get('search')
    
    if search_product:
        product_list = Product.objects.filter(Q(title__icontains=search_product))
        
    else:
        product_list = Product.objects.all()

    paginator = Paginator(product_list, 6)

    products = paginator.page(page)
    
    context = {
        'products': products
    }

    return render(request, 'store/home.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    comments = product.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'product': product,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(
        request,
        'store/product_detail.html',
        context,
    )


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {
        'category':category,
        'products':products,
    }

    return render(request, 'store/category.html', context)
