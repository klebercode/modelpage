# coding: utf-8
from django.shortcuts import get_object_or_404

from modelpage.core.models import Enterprise, Category, Area


def enterprise_proc(request):
    """ View Function """
    try:
        enterprise = get_object_or_404(Enterprise, pk=1)
    except:
        enterprise = ''

    area_list = Area.visibles.all()
    bot_list = Category.objects.filter(area__visible=True)
    menu_list = Category.objects.filter(area__visible=True, menu=True)
    menu_extra_list = Category.objects.filter(area__visible=True,
                                              menu_extra=True)

    return {
        'enterprise': enterprise,
        'area_list': area_list,
        'bot_list': bot_list,
        'menu_list': menu_list,
        'menu_extra_list': menu_extra_list,
    }


class EnterpriseExtraContext(object):
    """ Class Based View """
    try:
        enterprise = get_object_or_404(Enterprise, pk=1)
    except:
        enterprise = ''

    area_list = Area.visibles.all()
    bot_list = Category.objects.filter(area__visible=True)
    menu_list = Category.objects.filter(area__visible=True, menu=True)
    menu_extra_list = Category.objects.filter(area__visible=True,
                                              menu_extra=True)

    extra_context = {
        'enterprise': enterprise,
        'area_list': area_list,
        'bot_list': bot_list,
        'menu_list': menu_list,
        'menu_extra_list': menu_extra_list,
    }

    def get_context_data(self, **kwargs):
        context = super(EnterpriseExtraContext,
                        self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
