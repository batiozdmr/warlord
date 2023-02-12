from django.contrib.auth.models import Permission
from django.shortcuts import redirect

from core import settings


def permissionCheck(modelInfo, permissionInfo):
    def methodWrap(viewMethod):

        def wrap(request, *args, **kwargs):
            status = False
            permissions = Permission.objects.filter(group__user=request.user).filter(
                content_type__model=modelInfo).filter(
                codename=permissionInfo)
            if permissions:
                status = True
            elif request.user.is_staff:
                status = True
            else:
                status = False

            if not status:
                return redirect(settings.PERMISSION_DENIED_PAGE_URL)

            return viewMethod(request, *args, **kwargs)

        return wrap

    return methodWrap
