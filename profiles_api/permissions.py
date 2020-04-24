from rest_framework import permissions


class AllowOwnUpdate(permissions.BasePermission):
    """ permission to update only his own profile """

    def has_object_permission(self, request, view, obj):
        """ checks if the orofile is that of the logged in user """
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.id == request.user.id


class AllowEditOwnStatus(permissions.BasePermission):
    """ aloow user to modify only the statuses linked to his profile"""

    def has_object_permission(self,request,view,obj):
        """ checks if user is trying to edit his own status"""
        if request.method == permissions.SAFE_METHODS:
            return True
        else:
            return obj.user_profile.id == request.user.id    