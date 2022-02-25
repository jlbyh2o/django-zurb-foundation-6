from django.urls import path
from django.views.generic import TemplateView

# Test patern, renders Zurb Foundation default page using base template
urlpatterns = [
    path('', TemplateView.as_view(template_name="foundation/index.html"),
         name="foundation_index"),

    path('icons', TemplateView.as_view(template_name="foundation/icons.html"),
         name="foundation_icons"),
]
