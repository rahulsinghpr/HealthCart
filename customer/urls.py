from django.urls import path
from customer.views import CustomerSignup

urlpatterns = [
    path("", CustomerSignup.as_view()),
]
