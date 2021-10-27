from django.db.models import Count

from .models import *

menu = [{'title': "", 'url_name': 'about'},
        {'title': "Д", 'url_name': 'add_page'},
        {'title': "О", 'url_name': 'contact'},
]

class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
