from category.models import Category
from configuration.models import Configuration


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
    context = {
        "categories": categories,
        "sizes": sizes,
        "colors": colors,
        "config": config
    }
    return context
