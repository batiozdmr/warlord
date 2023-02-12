from django.contrib.auth.models import Group
from django.utils.translation import get_language

from apps.mainpage.models import MainPage
from apps.parameter.models import Menu, SiteSettings


def site(request):
    site_settings = SiteSettings.objects.last()
    main_page = MainPage.objects.last()
    urlObject = request.get_host()
    url = request.build_absolute_uri()
    return {'site_settings': site_settings, 'main_page': main_page, 'showURL': urlObject, 'URL': url,}


def menu(request):
    user_group = []
    if request.user.is_authenticated:
        user_group = Group.objects.filter(user=request.user)
    header_menu = Menu.objects.filter(menu_type_id=1, groupList__in=user_group).order_by('alignment')
    footer_menu = Menu.objects.filter(menu_type_id=2).order_by('alignment')
    lang = get_language()
    return {'header_menu': header_menu, 'footer_menu': footer_menu, 'lang': lang}
