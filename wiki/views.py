from django.shortcuts import render
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.
from django.http import HttpResponse
from wiki.forms import PageForm


def index(request):
    return HttpResponse("Hello, world. You're at the wiki's index.")

class PageList(ListView):
    """
        Assigned model to the page model we imported from modals.py
        stored a template we will be rendering in a variable
    CHALLENGES:
      1. On GET, display a homepage that shows all Pages in your wiki.
      2. Replace this CHALLENGE text with a descriptive docstring for PageList.
      3. Replace pass below with the code to render a template named `list.html`.
    """
    model = Page
    context_object_name = "pages"
    template_name = "page-list.html"
    # template_name = 'pages/list.html'

    # def get(self, request):
    #     """ Returns a list of wiki pages. """
    #     # return HttpResponse("Hello world!")
    #     # context = {
    #     #     "myvar": "some value"
    #     # }
    #     context = {
    #         'pages': Page.objects.all()
    #     }
    #     # print(context)
    #     # return context
    #     # return render(request, template_name, context)
    #     return render(request, 'page-list.html', context)


class PageDetailView(DetailView):
    """
    CHALLENGES:
      1. On GET, render a template named `page.html`.
      2. Replace this docstring with a description of what thos accomplishes.

    STRETCH CHALLENGES:
      1. Import the PageForm class from forms.py.
          - This ModelForm enables editing of an existing Page object in the database.
      2. On GET, render an edit form below the page details.
      3. On POST, check if the data in the form is valid.
        - If True, save the data, and redirect back to the DetailsView.
        - If False, display all the errors in the template, above the form fields.
      4. Instead of hard-coding the path to redirect to, use the `reverse` function to return the path.
      5. After successfully editing a Page, use Django Messages to "flash" the user a success message
           - Message Content: REPLACE_WITH_PAGE_TITLE has been successfully updated.
    """
    model = Page
    # context_object_name = "page"
    # template_name = "page-detail.html"
    # template_name = 'pages/page.html'

    def get(self, request, slug):
        """ Returns a specific of wiki page by slug. """
        # return HttpResponse("Hello World!"+slug)
        # pages = super().get(request)
        # print(pages)
        # return pages
        # pass
        print("In get method")
        context = {
            'page': Page.objects.get(slug=slug)

        }
        print("In get method after dict")
        return render(request, "page-detail.html", context)

    # def post(self, request, slug):
    #     # context = {
    #     #         'form': request.POST.get('model')
    #     #     }
    #     # return render(request, "page-detail.html", context)
    #     print("Hello World")
    #     form = Page(request.POST)
    #     if form.is_valid():
    #         print("Hello Mars")
    #         args = {
    #                 'model': request.POST.get('model')
    #         }
    #         return render(request, "page-post.html", args)
        # return HttpResponse("You're voting on question %s." % question_id)
