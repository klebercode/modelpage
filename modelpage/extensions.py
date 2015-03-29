# coding: utf-8

# from django.core.urlresolvers import reverse_lazy

# from grappelli_extensions.nodes import CLNode


class Navbar(object):
    nodes = (
        ('Gerenciador de Arquivos', {
            'url': 'filebrowser/browse',
        }),
    )


# class Sidebar(object):
#     nodes = (
#         ('Administração', {'nodes': (
#             ('Usuários', {
#                 'url': reverse_lazy('admin:auth_user_changelist'),
#                 'perm': 'auth.change_user',
#             }),
#             ('Grupos', {
#                 'url': reverse_lazy('admin:auth_group_changelist'),
#                 'perm': 'auth.change_group',
#             }),
#         )}),
#         # ('Sites',
#         #     {'url': reverse_lazy('admin:sites_site_changelist')}),
#         # ('Nodes', {'nodes': (
#         #     CLNode('auth', 'user'),
#         #     CLNode('sites', 'site'),
#         # )}),
#         # CLNode('auth', 'user', u"Site users"),
#     )
