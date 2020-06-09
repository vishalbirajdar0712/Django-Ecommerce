from products.models import Category, Product


def categories_processor(request):
    category = Category.objects.all()
    return {'category': category}


def product_processor(request):
    product = Product.objects.all()
    return {'product': product}