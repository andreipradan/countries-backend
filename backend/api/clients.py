import logging
import time

import telegram
from django.conf import settings
from telegram.constants import ParseMode


logger = logging.getLogger(__name__)


def send_telegram_message(text, retries_on_network_error=3, **kwargs):
    if not (chat_id := settings.TELEGRAM_CHAT_ID):
        logger.error("TELEGRAM_CHAT_ID not set on env")
        return None
    if not (token := settings.TELEGRAM_TOKEN):
        logger.error("TELEGRAM_TOKEN not set on env")
        return None

    bot_kwargs = {
        "chat_id": chat_id,
        "disable_notification": True,
        "disable_web_page_preview": True,
        "parse_mode": ParseMode.MARKDOWN,
    }
    bot_kwargs.update(kwargs)
    bot = telegram.Bot(token)
    try:
        return bot.send_message(text=text, **bot_kwargs)
    except telegram.error.NetworkError as e:
        if not isinstance(e, telegram.error.BadRequest):
            if "[Errno -3] Temporary failure in name resolution" not in str(e):
                raise e
            time.sleep(5)
            return send_telegram_message(
                text,
                retries_on_network_error=retries_on_network_error - 1,
                **bot_kwargs,
            )

        if "can't find end of the entity" in str(e):
            location = int(e.message.split()[-1])
            logger.warning("Error parsing markdown - skipping '%s'", text[location])
            text = f"{text[location:]}{text[location + 1 :]}"
            return send_telegram_message(text, chat_id=chat_id, logger=logger)
        logger.warning("Error sending message. Trying unformatted. (%s)", e)
        try:
            return bot.send_message(text=text, **{**bot_kwargs, "parse_mode": None})
        except telegram.error.BadRequest as err:
            logger.exception("Error sending unformatted message. (%s)", err)
