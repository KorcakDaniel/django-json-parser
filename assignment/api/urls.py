from django.urls import path
from api import views

urlpatterns = [
    path("import/", views.importData),
    path("detail/<str:model_name>/", views.getModel),
    path("detail/<str:model_name>/<int:id>", views.getEntry),
]
