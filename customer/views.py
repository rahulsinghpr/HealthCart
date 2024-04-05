from django.shortcuts import render
from django.views import View


class CustomerSignup(View):

    def get(self,request):
        return render(request,'customer/signup.html')
