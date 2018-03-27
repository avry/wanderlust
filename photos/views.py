from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . models import Post, Photo

# Create your views here.
def photo_list(request):
	queryset = Post.objects.all()
	
	paginator = Paginator(queryset, 10) # Show 10 contacts per page
	page_request_var = 'page'
	page = request.GET.get(page_request_var)
	queryset = paginator.get_page(page)
	context = {
		"objects_list": queryset,
		"page_request_var": page_request_var
	}

	return render(request, "post_list.html", context)


def post_detail(request, id=None):
	instance = get_object_or_404(Post, id = id)
	post_content = Photo.objects.filter(post = instance)
	context = {
		"instance": instance,
		"post_content": post_content
	}
	return render(request, "post_detail.html", context)