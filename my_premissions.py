from rest_framework.permissions import BasePermission


class IsMyPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'MODERATOR'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.publisher and obj.genre == 3


class IsAllowedToGetStatistic(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('can_get_statistic')