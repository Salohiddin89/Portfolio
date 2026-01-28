from django import template
import re

register = template.Library()


@register.filter
def youtube_embed(url):
    """
    YouTube URL ni embed formatga o'zgartiradi
    Shorts, watch va boshqa formatlarni qo'llab-quvvatlaydi
    """
    if not url:
        return url

    # YouTube Shorts formatini tekshirish
    shorts_match = re.search(r"youtube\.com/shorts/([a-zA-Z0-9_-]+)", url)
    if shorts_match:
        video_id = shorts_match.group(1)
        return (
            f"https://www.youtube-nocookie.com/embed/{video_id}?rel=0&modestbranding=1"
        )

    # Embed/shorts formatini tekshirish
    embed_shorts_match = re.search(r"youtube\.com/embed/shorts/([a-zA-Z0-9_-]+)", url)
    if embed_shorts_match:
        video_id = embed_shorts_match.group(1)
        return (
            f"https://www.youtube-nocookie.com/embed/{video_id}?rel=0&modestbranding=1"
        )

    # Oddiy watch formatini tekshirish
    watch_match = re.search(r"youtube\.com/watch\?v=([a-zA-Z0-9_-]+)", url)
    if watch_match:
        video_id = watch_match.group(1)
        return (
            f"https://www.youtube-nocookie.com/embed/{video_id}?rel=0&modestbranding=1"
        )

    # youtu.be formatini tekshirish
    short_match = re.search(r"youtu\.be/([a-zA-Z0-9_-]+)", url)
    if short_match:
        video_id = short_match.group(1)
        return (
            f"https://www.youtube-nocookie.com/embed/{video_id}?rel=0&modestbranding=1"
        )

    # Agar embed format bo'lsa
    if "youtube.com/embed/" in url:
        # Video ID ni olish
        video_id_match = re.search(r"embed/([a-zA-Z0-9_-]+)", url)
        if video_id_match:
            video_id = video_id_match.group(1)
            return f"https://www.youtube-nocookie.com/embed/{video_id}?rel=0&modestbranding=1"

    # Agar faqat video ID berilgan bo'lsa
    if re.match(r"^[a-zA-Z0-9_-]{11}$", url):
        return f"https://www.youtube-nocookie.com/embed/{url}?rel=0&modestbranding=1"

    return url


@register.filter
def get_video_id(url):
    """YouTube URL dan video ID ni oladi"""
    if not url:
        return ""

    patterns = [
        r"youtube\.com/shorts/([a-zA-Z0-9_-]+)",
        r"youtube\.com/embed/(?:shorts/)?([a-zA-Z0-9_-]+)",
        r"youtube\.com/watch\?v=([a-zA-Z0-9_-]+)",
        r"youtu\.be/([a-zA-Z0-9_-]+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    # Agar to'g'ridan-to'g'ri ID bo'lsa
    if re.match(r"^[a-zA-Z0-9_-]{11}$", url):
        return url

    return ""
