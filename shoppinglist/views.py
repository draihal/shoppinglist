from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Shoppinglist

from social_django.models import UserSocialAuth


@login_required
def homepageview(request):
    return redirect('/shoppinglist/')


@login_required
def shoppinglistview(request):
    try:
        github_login = request.user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    all_shoppinlist_items = Shoppinglist.objects.filter(owner=request.user.id)
    return render(request, 'shoppinglist.html', {
        'all_items': all_shoppinlist_items,
        'github_login': github_login,
    })


@login_required
def addshoppinglistitem(request):
    new_item = Shoppinglist(shoppinglist_item=request.POST['content'],
                            owner=request.user)
    new_item.save()
    return redirect('/shoppinglist/')


@login_required
def doneshoppinglistitem(request, shoppinglist_item_id):
    item_to_done = Shoppinglist.objects.get(id=shoppinglist_item_id)
    item_to_done.done = True
    item_to_done.save(update_fields=['done'])
    return redirect('/shoppinglist/')


@login_required
def undoneshoppinglistitem(request, shoppinglist_item_id):
    item_to_undone = Shoppinglist.objects.get(id=shoppinglist_item_id)
    item_to_undone.done = False
    item_to_undone.save(update_fields=['done'])
    return redirect('/shoppinglist/')


@login_required
def deleteshoppinglistitem(request, shoppinglist_item_id):
    item_to_delete = Shoppinglist.objects.get(id=shoppinglist_item_id)
    item_to_delete.delete()
    return redirect('/shoppinglist/')
