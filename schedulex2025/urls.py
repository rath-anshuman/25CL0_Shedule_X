from django.contrib import admin
from django.urls import path,include

from notes.views import notes,notessec

urlpatterns = [
    path('', admin.site.urls),
    path('api/notes/',notes),
    path('api/notes/<str:sec>',notessec)
]
