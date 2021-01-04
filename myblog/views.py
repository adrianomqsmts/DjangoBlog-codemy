from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.

# def home(request):
#   return render(request, 'home.html', {})


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    #fields = '__all__'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if(post.likes.filter(id=request.user.id).exists()):
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))


class HomeListView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-post_date']

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryListView(TemplateView):
    template_name = "category.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        cat = self.kwargs['cats'].replace('-', ' ')
        context['posts'] = Post.objects.filter(category__icontains=cat)
        context['category'] = cat
        context['categories'] = Category.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        context['total_likes'] = stuff.total_likes()

        liked = False
        if(stuff.likes.filter(id=self.request.user.id)):
            liked = True
        context['liked'] = liked

        return context


class AddPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(AddPostCreateView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryCreateView(CreateView):
    model = Category
    template_name = "add_category.html"
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    # fields = ['title', 'title', 'body']

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(PostDeleteView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
