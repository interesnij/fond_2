from django.views.generic.base import TemplateView
from about.forms import FeedbackForm
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from generic.mixins import CategoryListMixin


class AboutView(TemplateView, CategoryListMixin):
    template_name = "about.html"

    def get_context_data(self,**kwargs):
        context=super(AboutView,self).get_context_data(**kwargs)
        context["form"] = FeedbackForm()
        return context

class FeedbackView(View):
    def post(self,request,*args,**kwargs):
        form = FeedbackForm(request.POST)
        if request.is_ajax() and form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            recipients = ['my_name_aleksandra@mail.ru']
            try:
                send_mail('На сайте aleksandra.top оставили сообщение', 'Написал "{}", почта "{}", сообщение "{}"'.format(name, email, message), settings.EMAIL_HOST_USER, recipients)
                send_mail('Спасибо за сообщение на сайте aleksandra.top', 'Дорогой {}, Спасибо, что оставили сообщение на сайте aleksandra.top. Мы рады любому отзыву или обращению!'.format(name), settings.EMAIL_HOST_USER, [email])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse ()
        else:
            return HttpResponseBadRequest()
