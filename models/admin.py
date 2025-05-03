from django.contrib import admin
from .models import User, Task, TaskReassign


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("Id", "TgName", "Name", "PhoneNumber", "Role", "TaskCount", "CreatedAt")
    list_filter = ("Role", "CreatedAt")
    search_fields = ("TgName", "Name", "PhoneNumber")
    readonly_fields = ("Id", "CreatedAt", "UpdatedAt")
    ordering = ("Id",)

    fieldsets = (
        ("User Information", {"fields": ("Id", "TgId", "TgName", "Name", "PhoneNumber")}),
        ("Activity", {"fields": ("TaskCount", "Role")}),
        ("Timestamps", {"fields": ("CreatedAt", "UpdatedAt"), "classes": ("collapse",)}),
    )

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_change_permission(self, *args, **kwargs):
        return False


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("Id", "Company", "Author", "Worker", "RequestDate", "StartDate", "EndDate", "IsReassigned")
    list_filter = ("IsReassigned", "RequestDate", "StartDate", "EndDate")
    search_fields = ("Company", "Author", "Worker", "Message")
    readonly_fields = ("Id", "CreatedAt", "UpdatedAt")
    ordering = ("Id",)

    fieldsets = (
        ("Task Details", {"fields": ("Id", "Company", "Message")}),
        ("People", {"fields": ("Author", "AuthorId", "Worker", "WorkerId")}),
        ("Timeline", {"fields": ("RequestDate", "StartDate", "EndDate")}),
        ("Telegram Info", {"fields": ("GroupId", "MessageId"), "classes": ("collapse",)}),
        ("Status", {"fields": ("IsReassigned", "Confirmation")}),
        ("Timestamps", {"fields": ("CreatedAt", "UpdatedAt"), "classes": ("collapse",)}),
    )

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_change_permission(self, *args, **kwargs):
        return False


@admin.register(TaskReassign)
class TaskReassignAdmin(admin.ModelAdmin):
    list_display = ("Id", "TaskId", "Appointer", "Executor", "Hours", "StartDate", "EndDate", "IsDone")
    list_filter = ("IsDone", "StartDate", "EndDate")
    search_fields = ("Appointer", "Executor")
    readonly_fields = ("Id", "CreatedAt", "UpdatedAt")
    ordering = ("Id",)

    fieldsets = (
        ("Assignment Details", {"fields": ("Id", "TaskId")}),
        ("People", {"fields": ("Appointer", "AppointerId", "Executor", "ExecutorId")}),
        ("Work Details", {"fields": ("Hours", "StartDate", "EndDate", "IsDone")}),
        ("Timestamps", {"fields": ("CreatedAt", "UpdatedAt"), "classes": ("collapse",)}),
    )

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_change_permission(self, *args, **kwargs):
        return False
