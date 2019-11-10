from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from .models import Post
from .forms import NewPostForm

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailsView(DetailView):
    model = Post
    template_name = 'post_details.html'

class PostEditView(UpdateView):
    model = Post
    fields = ('title', 'body')
    template_name = 'post_new.html'
    def get_success_url(self, **kwargs):
        return reverse("post_details", kwargs={'pk': self.object.pk})

def post_new(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('home')
    else:
        form = NewPostForm()
    return render(request, 'post_new.html', {'form': form})
    

