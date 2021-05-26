from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Post, AdditionalImage, Comment
from .forms import UserCommentForm
from django.contrib import messages


class BlogListView(ListView):

    model = Post
    comment = Comment 
    template_name = 'home.html'


class BlogDetailView(DetailView):

    model = Post
    image = AdditionalImage
    comment = Comment 
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):

    model = Post
    image = AdditionalImage
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):

    model = Post
    image = AdditionalImage
    template_name = 'post_edit.html'
    fields = ['title', 'body']    

class BlogDeleteView(DeleteView):

    model = Post
    image = AdditionalImage
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    ais = post.additionalimage_set.all()
    comments = Comment.objects.filter(post = pk)
    initial = {'post': post.pk}
    form_class = UserCommentForm
    form = form_class(initial=initial)

    if request.method == 'POST':
        comment_form = form_class(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            messages.add_message(request, messages.SUCCESS, 'Комментарий добавлен')
        else:
            form = comment_form
            messages.add_message(request, messages.WARNING, 'Комментарий недобавлен')

    context = {'post':post, 'ais':ais, 'form':form, 'comments': comments, }
    return render(request, 'post_detail.html', context) 