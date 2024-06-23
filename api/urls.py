from django.urls import path, include

from .views.item import *

urlpatterns = [
    # model item
    path('item/', include([
        path('all', ListItemAPIView.as_view()),
        path('create', CreateItemAPIView.as_view()),
        path('<int:pk>/', include([
            path('', GetItemAPIView.as_view()),
            path('update', UpdateItemAPIView.as_view()),
            path('delete', DeleteItemAPIView.as_view()),
        ]))
    ])),
]