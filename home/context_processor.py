from django.shortcuts import get_object_or_404
from home.models import Profile

""" Function to check if user is a premium member """
def is_premium_member(request):
    profile = get_object_or_404(Profile, email=request.user.email)
    if profile.premium_member:
        return True
    else:
        return False