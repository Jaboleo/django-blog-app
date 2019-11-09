from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Post
from .forms import NewPostForm

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

def post_new(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('home')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'form': form})
    

