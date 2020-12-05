from django.shortcuts import render
from blog.models import Post, Contact

# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all()
    }   
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        message = request.POST.get("query")
        entry = Contact(name=name, email=email, phone_num=phone_number, message=message)
        entry.save()
        
    return render(request, "contact.html")

def post(request, sno):
    context = {
        'post': Post.objects.filter(sno=sno).first()
    }
    return render(request, "post.html", context)

def search(request):
    category = request.GET.get("category")
    context = {
        'posts': Post.objects.filter(post_category=category),
        'length': len(Post.objects.filter(post_category=category)),
        'category': category
    }
    return render(request, "search.html", context)