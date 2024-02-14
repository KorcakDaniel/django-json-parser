from django.urls import path
from api import views

urlpatterns = [
    path("import/", views.import_data),
    path("detail/<str:model_name>/", views.get_model),
    path("detail/<str:model_name>/<int:id>", views.get_entry),
]
