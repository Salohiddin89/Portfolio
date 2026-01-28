import requests
from django.conf import settings


def send_telegram_message(full_name, phone, message):
    """
    Telegram botga xabar yuborish
    """
    # Telegram bot token va chat ID ni settings.py ga qo'shing
    bot_token = getattr(settings, "TELEGRAM_BOT_TOKEN", "")
    chat_id = getattr(settings, "TELEGRAM_CHAT_ID", "")

    if not bot_token or not chat_id:
        print("⚠️ Telegram bot sozlamalari topilmadi!")
        return False

    # Xabarni formatlash
    text = f"""
🆕 Yangi Xabar Portfolio Saytidan!

👤 Ism: {full_name}
📱 Telefon: {phone}

💬 Xabar:
{message}

📅 Vaqt: {message}
    """

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    data = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}

    try:
        response = requests.post(url, data=data, timeout=10)
        if response.status_code == 200:
            print("✅ Xabar Telegramga yuborildi!")
            return True
        else:
            print(f"❌ Xatolik: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Xatolik: {str(e)}")
        return False
