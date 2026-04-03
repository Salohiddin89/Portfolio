from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language
from django.utils.translation import gettext as _
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Project, Blog, Skill, ContactMessage
from .telegram_bot import send_telegram_message
import json


def home(request):
    lang = get_language()
    projects = Project.objects.all()
    blogs = Blog.objects.all()[:6]
    skills = Skill.objects.all()

    context = {
        "projects": projects,
        "blogs": blogs,
        "skills": skills,
        "current_lang": lang,
    }
    return render(request, "portfolio/home.html", context)


def project_detail(request, pk):
    lang = get_language()
    project = get_object_or_404(Project, pk=pk)
    return render(
        request,
        "portfolio/project_detail.html",
        {"project": project, "current_lang": lang},
    )


def blog_detail(request, pk):
    lang = get_language()
    blog = get_object_or_404(Blog, pk=pk)
    return render(
        request, "portfolio/blog_detail.html", {"blog": blog, "current_lang": lang}
    )


@require_POST
@csrf_exempt
def send_message(request):
    try:
        data = json.loads(request.body)
        full_name = data.get("full_name", "").strip()
        phone = data.get("phone", "").strip()
        message = data.get("message", "").strip()

        # Validatsiya
        if not full_name or not phone or not message:
            return JsonResponse(
                {
                    "success": False,
                    "message": _("Iltimos, barcha maydonlarni to'ldiring"),
                },
                status=400,
            )

        # Bazaga saqlash
        contact = ContactMessage.objects.create(
            full_name=full_name, phone=phone, message=message
        )

        # Telegramga yuborish
        telegram_sent = send_telegram_message(full_name, phone, message)

        if telegram_sent:
            contact.is_sent_to_telegram = True
            contact.save()

        return JsonResponse(
            {
                "success": True,
                "message": _(
                    "Xabaringiz muvaffaqiyatli yuborildi! Tez orada siz bilan bog'lanamiz."
                ),
            }
        )

    except Exception as e:
        return JsonResponse(
            {
                "success": False,
                "message": _("Xatolik yuz berdi. Iltimos, qayta urinib ko'ring."),
            },
            status=500,
        )


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Allow: /",
        "",
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
