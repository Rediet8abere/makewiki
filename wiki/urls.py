from django.urls import path
from .views import PageList, PageDetailView, PageCreateView

"""
  CHALLENGES:
    1. Refactor the URL named `wiki-list-page` and point it to the root route (`/`).
      - Make sure Django doesn't give you any warnings or errors when you execute `python manage.py runserver`.
      - Test by visiting http://127.0.0.1:8000/.
    2. Refactor the URL named `wiki-details-page` to show the DetailsView for any Page that exists.
      - Use the slug field in the Page model to accomplish this.
      - DO NOT CHANGE the `name` argument.
      - Test by visiting http://127.0.0.1:8000/w/title-but-replace-spaces-with-dashes in your browser.
  """


#
urlpatterns = [
    # path('', views.index, name='index'),
    path('', PageList.as_view(), name='wiki-list-page'),
    path('create/', PageCreateView.as_view(), name='wiki-create-page'),
    path('<slug>/', PageDetailView.as_view(), name='wiki-details-page'),
    path('post/new/', PageDetailView.as_view(), name='post_new'),
]
