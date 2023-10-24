# flake8: noqa

from blog.models import Page, Post
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
PER_PAGE = 9


def index(request):

    posts = (
        Post.objects
        .filter(is_published=True)
        .order_by('-pk'))

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': 'Início - ',
        }
    )


def created_by(request, author_pk):

    posts = (
        Post.objects
        .filter(created_by__pk=author_pk)
    )

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': 'Posts - ',
        }
    )


def category(request, slug):
    posts = (
        Post.objects
        .filter(category__slug=slug)
    )

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': 'Categoria - ',
        }
    )


def tag(request, slug):
    posts = (
        Post.objects
        .filter(tags__slug=slug)
    )

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': 'Tags - ',
        }
    )


def search(request):

    search_value = request.GET.get('search', '').strip()
    posts = (
        Post.objects
        .filter(
            Q(title__icontains=search_value) |
            Q(excerpt__icontains=search_value) |
            Q(content__icontains=search_value)
        )[:PER_PAGE]
    )

    # paginator = Paginator(posts, PER_PAGE)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': posts,
            'search_value': search_value,
            'page_title': 'Busca - ',
        }
    )


def page(request, slug):
    page = (
        Page.objects
        .filter(is_published=True)
        .filter(slug=slug)
        .first()
    )

    return render(
        request,
        'blog/pages/page.html',
        {
            'page': page,
        }
    )


def post(request, slug):
    post = (
        Post.objects
        .filter(slug=slug)
        .first()
    )

    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post,
            'page_title': 'Post - ',
        }
    )
