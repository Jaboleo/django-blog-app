from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView
from .models import Post
from .forms import NewPostForm
from datetime import datetime

# Create your views here.
class HomePageView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'home.html'

class PostDetailsView(DetailView):
    model = Post
    template_name = 'posts/post_details.html'

class PostEditView(UpdateView):
    model = Post
    fields = ('title', 'body')
    template_name = 'posts/post_edit.html'
    def get_success_url(self, **kwargs):
        return reverse("post_details", kwargs={'pk': self.object.pk})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    def get_success_url(self):
        return reverse('home')

def post_new(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = NewPostForm()
    return render(request, 'posts/post_new.html', {'form': form})
    

