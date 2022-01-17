from category.models import Category
from configuration.models import Configuration
from cart.models import Cart, CartItem


def get_categories(request):
    categories = Category.objects.all()
    config = Configuration.objects.all()[0]
    colors = [
        {'key': 'R', 'value': 'Red'},
        {'key': 'G', 'value': 'Green'},
        {'key': 'W', 'value': 'While'},
        {'key': 'B', 'value': 'Black'},
        {'key': 'P', 'value': 'Pink'},
    ]

    sizes = [
        {'key': 'S', 'value': 'Small'},
        {'key': 'M', 'value': 'Medium'},
        {'key': 'L', 'value': 'Large'},
        {'key': 'X', 'value': 'Extra Large'},
    ]
    cart_count = 0
    if request.user.is_authenticated:
        user_id = request.user.id
        cart_count = CartItem.objects.select_related('cart').filter(cart__user=user_id, cart__status=1).count()
    context = {
        "categories": categories,
        "sizes": sizes,
        "colors": colors,
        "config": config,
        "cart_count": cart_count
    }
    return context
