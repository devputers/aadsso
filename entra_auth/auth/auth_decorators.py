from functools import wraps
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from entra_auth.views import  microsoft_logout


def is_member(user, group_names):
    print("user oss", user)
    print(user.groups)
    print(group_names)
    #check user with costom user 
    from webUI.models import User,Group,User_Groups
    try:
        user = User.objects.get(username=user)
        group = Group.objects.get(name=group_names[0])  
        print("in check",user,group)
        # Check if the user is in the group
        if User_Groups.objects.filter(user_id=user.id, group_id=group.id).exists():
            print(f"{user} is in group {group_names[0]}")
            return user
        else:
            print(f"{user} is not in group {group_names[0]}")
            return False
    except User.DoesNotExist:
        print(f"User '{user}' not found")
        return False
    except Group.DoesNotExist:
        print(f"Group '{group_names[0]}' not found")
        return False
    except Exception as e:
        print("Error in check user",str(e))
        return False
    #
    # return user.groups.filter(name__in=group_names).exists() if user else False

    # experiment deleted
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



def login_required_with_AD(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):

        ans=  is_member(
            user=request.user,
            group_names=('mssso',)
        )
        print('ans_',ans)
        if ans:
            if not request.user.is_authenticated:
                return redirect("/entra_auth/login")
        else:
            if request.user.is_authenticated:
                microsoft_logout(request)
                return HttpResponseForbidden("Group Not exist. Not authorized.")
      
        # Call the original login_required decorator
        print(request.get_full_path())
        return login_required(view_func)(request, *args, **kwargs)

    return _wrapped_view
