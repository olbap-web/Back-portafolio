from django.shortcuts import render

from django.views import View
# Create your views here.
class IndexPageView(View):

    template_name = 'core/index.html'
    
    def get(self, request):

        return render(request, self.template_name)