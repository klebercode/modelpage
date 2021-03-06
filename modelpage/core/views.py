# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from modelpage.context_processors import enterprise_proc

from modelpage.core.models import (Link, Program, Banner, Category, Content,
                                   Timeline)
from modelpage.event.models import Calendar
from modelpage.blog.models import Entry
from modelpage.channel.models import Video

from modelpage.core.forms import ContactForm


def home(request):
    context = {}
    context['link_list'] = Link.objects.all()
    context['program_list'] = Program.objects.all()
    context['calendar_list'] = Calendar.objects.all()[:4]
    context['blog_list'] = Entry.published.all()[:6]
    context['blog_focused_list'] = Entry.focused.all()[:3]
    context['super_banner_list'] = Banner.published.filter(type=1)
    context['second_banner_list'] = Banner.published.filter(type=2)
    context['popup_banner_list'] = Banner.published.filter(type=3)[:1]
    context['video_list'] = Video.objects.all()[:5]

    return render(request, 'home.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


def construction(request):
    context = {}

    return render(request, 'construction.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


def contact(request):
    context = {}

    # contact
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_mail()
            context['contact_success'] = True
    else:
        form = ContactForm()

    context['contact_form'] = form

    return render(request, 'contact.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


def content(request, slug):
    context = {}

    category = Category.objects.filter(slug=slug)

    content_list = get_object_or_404(Content, category=category)
    # try:
    # except:
    #     content_list = ''

    context['content_list'] = content_list
    context['blog_list'] = Entry.published.filter(categories=category)[:6]
    context['category_list'] = Category.objects.filter(
        area__home=True).order_by('?')[:10]
    context['last_video_list'] = Video.objects.all()[:4]

    return render(request, 'content.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


def city(request):
    context = {}

    context['timeline_list'] = Timeline.objects.all()

    return render(request, 'institutional.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


def transparency(request):
    context = {}

    pagina = request.GET.get('pagina', '')
    if pagina:
        context['pagina'] = pagina

    return render(request, 'transparencia.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))
    # return redirect('http://palmeirina.pe.gov.br/transparencia/')
