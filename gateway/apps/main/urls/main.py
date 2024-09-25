from django.urls import path
from apps.main.views import GetBookDetailView, GetBookView

urlpatterns = [
    path('book/<int:pk>/', GetBookDetailView.as_view(), name='Book-Detail'),
    path('book/', GetBookView.as_view(), name='Book'),
]

