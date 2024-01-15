from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import redirect


def is_member(user, group_names):
    return user.groups.filter(name__in=group_names).exists() if user else False

    # from django.contrib.auth.models import User
    # print(user)
    # print(user.groups)
    # print(group_names)
    # try:
    #     user = User.objects.get(username=user)
    # except User.DoesNotExist:
    #     return HttpResponse("User not found")
    # return user.groups.filter(name__in=group_names).exists() if user else False
    # print(user.groups.filter(name=group_names).exists())
    # return user.groups.filter(name__in=group_names).exists()
    # groups = user.groups.all()
    # result = any(grp.name in group_names for grp in groups)
    # return result


def microsoft_login_required(groups=None):
    """
    A user can only access page if
    the user belongs to the given group.
    """
    def _wrapper(view_func):
        def _view_wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("/entra_auth/login")
            if groups:
                if is_member(
                    user=request.user,
                    group_names=groups
                ):
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponseForbidden("Not authorized.")
            return view_func(request, *args, **kwargs)
        return _view_wrapper
    return _wrapper
