from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from .models import Category, Post, Comment
from .forms import CommentForm


def blog_posts(request, tag_slug=None):
    """ A view to show the blog list page """

    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags=tag.id)

    paginator = Paginator(posts, 2)
    page = request.GET.get("page", 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "posts": posts,
        "categories": categories,
        'tag': tag,
        "tags": tags,
    }

    return render(request, "blog/blog_posts.html", context)


def post_detail(request, slug):
    """ A view to show the blog post page """

    post = Post.objects.get(slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request,
                  'blog/post_detail.html',
                  {'post': post,
                   'form': form,
                   'categories': categories,
                   'tags': tags}
                  )