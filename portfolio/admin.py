from django.contrib import admin
from .models import Project, Blog, Skill


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name_uz", "client_uz", "created_at"]
    list_filter = ["created_at"]
    search_fields = [
        "name_uz",
        "name_ru",
        "name_en",
        "short_description_uz",
        "client_uz",
    ]
    date_hierarchy = "created_at"

    fieldsets = (
        ("Asosiy ma'lumotlar", {"fields": ("image", "url")}),
        (
            "O'zbek tili",
            {
                "fields": (
                    "name_uz",
                    "short_description_uz",
                    "full_description_uz",
                    "client_uz",
                )
            },
        ),
        (
            "Rus tili",
            {
                "fields": (
                    "name_ru",
                    "short_description_ru",
                    "full_description_ru",
                    "client_ru",
                )
            },
        ),
        (
            "Ingliz tili",
            {
                "fields": (
                    "name_en",
                    "short_description_en",
                    "full_description_en",
                    "client_en",
                )
            },
        ),
    )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title_uz", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title_uz", "title_ru", "title_en", "description_uz"]
    date_hierarchy = "created_at"

    fieldsets = (
        ("Asosiy ma'lumotlar", {"fields": ("image",)}),
        (
            "Video",
            {
                "fields": ("video_url", "video_file"),
                "description": "Video URL yoki video faylni yuklang. Ikkalasi ham bo'lsa, ikkalasi ham ko'rsatiladi.",
            },
        ),
        ("O'zbek tili", {"fields": ("title_uz", "description_uz")}),
        ("Rus tili", {"fields": ("title_ru", "description_ru")}),
        ("Ingliz tili", {"fields": ("title_en", "description_en")}),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name_uz", "percentage", "order"]
    list_editable = ["percentage", "order"]
    ordering = ["order"]

    fieldsets = (
        ("Asosiy", {"fields": ("percentage", "order")}),
        ("O'zbek tili", {"fields": ("name_uz",)}),
        ("Rus tili", {"fields": ("name_ru",)}),
        ("Ingliz tili", {"fields": ("name_en",)}),
    )
