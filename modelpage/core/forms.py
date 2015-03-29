# coding: utf-8
from django import forms
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from decouple import config

from modelpage.core.models import Enterprise

class ContactForm(forms.Form):
    name = forms.CharField(label=u'Nome',
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Digite seu nome'}))
    phone = forms.CharField(label=u'Fone',
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Digite seu fone'}))
    email = forms.EmailField(label=u'E-mail',
                             widget=forms.TextInput(
                                 attrs={'placeholder': 'Digite seu e-mail'}))
    subject = forms.CharField(label=u'Assunto',
                              widget=forms.TextInput(
                                  attrs={'placeholder': 'Digite o assunto'}))
    message = forms.CharField(label=u'Mensagem',
                              widget=forms.Textarea(
                                  attrs={'placeholder': 'Digite a mensagem'}))

    def send_mail(self):
        subject = u'Contato do site (%s)' % self.cleaned_data['name']
        context = {
            'name': self.cleaned_data['name'],
            'phone': self.cleaned_data['phone'],
            'email': self.cleaned_data['email'],
            'subject': self.cleaned_data['subject'],
            'message': self.cleaned_data['message'],
        }
        from_mail = Enterprise.objects.get(pk=1)
        message = render_to_string('contact_mail.txt', context)
        message_html = render_to_string('contact_mail.html', context)
        msg = EmailMultiAlternatives(subject, message,
                                     config('DEFAULT_FROM_EMAIL'),
                                     [from_mail.email])

        msg.attach_alternative(message_html, 'text/html')
        msg.send()
