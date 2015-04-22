# coding: utf-8
from django.db.models import Q
from django.views import generic
from django.views.generic.dates import (YearArchiveView, MonthArchiveView,
                                        DayArchiveView)

from modelpage.context_processors import EnterpriseExtraContext

from modelpage.channel.models import Video, Audio
from modelpage.core.models import Category
from modelpage.event.models import Calendar
from modelpage.blog.models import Entry


class VideoYearArchiveView(YearArchiveView):
    queryset = Video.objects.all()
    date_field = 'created'
    make_object_list = True
    allow_future = True
    # TODO: mudar a paginacao
    paginate_by = 10


class VideoMonthArchiveView(MonthArchiveView):
    queryset = Video.objects.all()
    date_field = 'created'
    make_object_list = True
    allow_future = True


class VideoDayArchiveView(DayArchiveView):
    queryset = Video.objects.all()
    date_field = 'created'
    make_object_list = True
    allow_future = True


class VideoListView(EnterpriseExtraContext, generic.ListView):
    queryset = Video.objects.all()
    template_name = 'video/video_home.html'
    # TODO: mudar a paginacao
    paginate_by = 3

    def get_queryset(self, **kwargs):
        search = self.request.GET.get('search', '')
        if search:
            obj_lst = Video.objects.filter(Q(title__icontains=search) |
                                           Q(created__icontains=search) |
                                           Q(body__icontains=search))
        else:
            obj_lst = Video.objects.all()
        return obj_lst

    def get_context_data(self, **kwargs):
        context = super(VideoListView, self).get_context_data(**kwargs)
        search = self.request.GET.get('search', '')
        context['search'] = search
        context['tag_list'] = Video.tags.most_common()
        # TODO: mudar a forma de carregamento das categorias
        context['category_list'] = Category.objects.filter(
            area__home=True).order_by('?')[:10]
        context['calendar_list'] = Calendar.objects.all()[:4]
        context['blog_list'] = Entry.published.all()[:4]
        context['last_list'] = Video.objects.all().order_by('?')[:4]
        return context


class VideoDateDetailView(EnterpriseExtraContext, generic.DateDetailView):
    queryset = Video.objects.all()
    template_name = 'video/video_detail.html'
    date_field = 'created'
    make_object_list = True
    allow_future = True

    def get_context_data(self, **kwargs):
        context = super(VideoDateDetailView, self).get_context_data(**kwargs)
        context['tag_list'] = Video.tags.most_common()
        # TODO: mudar a forma de carregamento das categorias
        context['category_list'] = Category.objects.filter(
            area__home=True).order_by('?')[:10]
        context['calendar_list'] = Calendar.objects.all()[:4]
        context['blog_list'] = Entry.published.all()[:4]
        context['last_list'] = Video.objects.all()[:4]
        return context


class VideoTagListView(VideoListView):
    """
    Herda de VideoListView mudando o filtro para tag selecionada
    """
    def get_queryset(self):
        """
        Incluir apenas as Entries marcadas com a tag selecionada
        """
        return Video.objects.filter(tags__slug=self.kwargs['tag_slug'])


class VideoCategoryListView(VideoListView):
    """
    Herda de VideoListView mudando o filtro para categoria selecionada
    """
    def get_queryset(self, **kwargs):
        """
        Inclui apenas as Entries marcadas com a categoria selecionada
        """
        return Video.objects.filter(categories__slug=self.kwargs['cat_slug'])


class AudioListView(EnterpriseExtraContext, generic.ListView):
    queryset = Audio.objects.all()
    template_name = 'audio/audio_home.html'
    # TODO: mudar a paginacao
    paginate_by = 6

    def get_queryset(self, **kwargs):
        search = self.request.GET.get('search', '')
        if search:
            obj_lst = Audio.objects.filter(Q(title__icontains=search) |
                                           Q(created__icontains=search) |
                                           Q(body__icontains=search))
        else:
            obj_lst = Audio.objects.all()
        return obj_lst

    def get_context_data(self, **kwargs):
        context = super(AudioListView, self).get_context_data(**kwargs)
        search = self.request.GET.get('search', '')
        context['search'] = search
        context['tag_list'] = Audio.tags.most_common()
        # TODO: mudar a forma de carregamento das categorias
        context['category_list'] = Category.objects.filter(
            area__home=True).order_by('?')[:10]
        context['calendar_list'] = Calendar.objects.all()[:4]
        context['blog_list'] = Entry.published.all()[:4]
        context['last_list'] = Audio.objects.all().order_by('?')[:4]
        return context


class AudioDateDetailView(EnterpriseExtraContext, generic.DateDetailView):
    queryset = Audio.objects.all()
    template_name = 'audio/audio_detail.html'
    date_field = 'created'
    make_object_list = True
    allow_future = True

    def get_context_data(self, **kwargs):
        context = super(AudioDateDetailView, self).get_context_data(**kwargs)
        context['tag_list'] = Audio.tags.most_common()
        # TODO: mudar a forma de carregamento das categorias
        context['category_list'] = Category.objects.filter(
            area__home=True).order_by('?')[:10]
        context['calendar_list'] = Calendar.objects.all()[:4]
        context['blog_list'] = Entry.published.all()[:4]
        context['last_list'] = Audio.objects.all()[:4]
        return context


class AudioTagListView(AudioListView):
    def get_queryset(self):
        return Audio.objects.filter(tags__slug=self.kwargs['tag_slug'])


class AudioCategoryListView(AudioListView):
    def get_queryset(self, **kwargs):
        return Audio.objects.filter(categories__slug=self.kwargs['cat_slug'])
