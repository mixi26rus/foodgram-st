from rest_framework import permissions


class CanEditRecipeOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class CanDownloadShoppingCart(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
