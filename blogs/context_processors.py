from blogs.models import Category, SocialLink


def get_categories(request):
    categories=Category.objects.all()
    return dict(categories=categories)

def get_sociallinks(request):
    sociallinks=SocialLink.objects.all()
    return dict(sociallinks=sociallinks)
    