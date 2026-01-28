from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    name_uz = models.CharField(_("Nomi (O'zbek)"), max_length=200)
    name_ru = models.CharField(_("Nomi (Rus)"), max_length=200)
    name_en = models.CharField(_("Nomi (Ingliz)"), max_length=200)

    image = models.ImageField(_("Rasm"), upload_to="projects/")

    short_description_uz = models.TextField(_("Qisqa tavsif (O'zbek)"), max_length=300)
    short_description_ru = models.TextField(_("Qisqa tavsif (Rus)"), max_length=300)
    short_description_en = models.TextField(_("Qisqa tavsif (Ingliz)"), max_length=300)

    full_description_uz = models.TextField(_("To'liq tavsif (O'zbek)"))
    full_description_ru = models.TextField(_("To'liq tavsif (Rus)"))
    full_description_en = models.TextField(_("To'liq tavsif (Ingliz)"))

    client_uz = models.CharField(
        _("Kim uchun qilingan (O'zbek)"), max_length=200, blank=True
    )
    client_ru = models.CharField(
        _("Kim uchun qilingan (Rus)"), max_length=200, blank=True
    )
    client_en = models.CharField(
        _("Kim uchun qilingan (Ingliz)"), max_length=200, blank=True
    )

    url = models.URLField(_("URL manzil"), blank=True)
    created_at = models.DateTimeField(_("Yaratilgan"), auto_now_add=True)

    class Meta:
        verbose_name = _("Proyekt")
        verbose_name_plural = _("Proyektlar")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name_uz

    def get_name(self, lang):
        return getattr(self, f"name_{lang}", self.name_uz)

    def get_short_description(self, lang):
        return getattr(self, f"short_description_{lang}", self.short_description_uz)

    def get_full_description(self, lang):
        return getattr(self, f"full_description_{lang}", self.full_description_uz)

    def get_client(self, lang):
        return getattr(self, f"client_{lang}", self.client_uz)


class Blog(models.Model):
    title_uz = models.CharField(_("Sarlavha (O'zbek)"), max_length=200)
    title_ru = models.CharField(_("Sarlavha (Rus)"), max_length=200)
    title_en = models.CharField(_("Sarlavha (Ingliz)"), max_length=200)

    image = models.ImageField(_("Rasm"), upload_to="blogs/")

    description_uz = models.TextField(_("Tavsif (O'zbek)"))
    description_ru = models.TextField(_("Tavsif (Rus)"))
    description_en = models.TextField(_("Tavsif (Ingliz)"))

    video_url = models.URLField(_("Video URL"), blank=True)
    video_file = models.FileField(_("Video fayl"), upload_to="blog_videos/", blank=True)

    created_at = models.DateTimeField(_("Yaratilgan"), auto_now_add=True)

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Bloglar")
        ordering = ["-created_at"]

    def __str__(self):
        return self.title_uz

    def get_title(self, lang):
        return getattr(self, f"title_{lang}", self.title_uz)

    def get_description(self, lang):
        return getattr(self, f"description_{lang}", self.description_uz)


class Skill(models.Model):
    name_uz = models.CharField(_("Til nomi (O'zbek)"), max_length=100)
    name_ru = models.CharField(_("Til nomi (Rus)"), max_length=100)
    name_en = models.CharField(_("Til nomi (Ingliz)"), max_length=100)

    percentage = models.IntegerField(_("Foiz (0-100)"))
    order = models.IntegerField(_("Tartib"), default=0)

    class Meta:
        verbose_name = _("Ko'nikma")
        verbose_name_plural = _("Ko'nikmalar")
        ordering = ["order"]

    def __str__(self):
        return f"{self.name_uz} - {self.percentage}%"

    def get_name(self, lang):
        return getattr(self, f"name_{lang}", self.name_uz)


class ContactMessage(models.Model):
    full_name = models.CharField(_("Ism familiya"), max_length=200)
    phone = models.CharField(_("Telefon raqami"), max_length=20)
    message = models.TextField(_("Xabar"))
    created_at = models.DateTimeField(_("Yuborilgan vaqt"), auto_now_add=True)
    is_sent_to_telegram = models.BooleanField(_("Telegramga yuborildi"), default=False)

    class Meta:
        verbose_name = _("Xabar")
        verbose_name_plural = _("Xabarlar")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
