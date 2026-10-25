import logging
import os
import random

from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters


POEMS = (
    "В строке — короткий добрый след,\n"
    "И в чате вспыхнул тихий свет.\n"
    "Пускай заботы станут тише,\n"
    "А день — немного выше.",
    "Пришло послание — привет,\n"
    "В ответ летит простой куплет.\n"
    "Пусть будет в мыслях ясный лад,\n"
    "И каждый миг пусть будет рад.",
    "Слова плывут, как ручеёк,\n"
    "И складываются в стишок.\n"
    "Пусть улыбнётся этот час,\n"
    "И добрый ритм поддержит вас.",
    "Пускай сообщение твоё\n"
    "Найдёт поэзию свою.\n"
    "Четыре строчки — и привет,\n"
    "Пусть в них живёт хороший свет.",
)


async def reply_with_poem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reply to each incoming Telegram message with a short poem."""
    message = update.effective_message
    if message is None:
        return

    await message.reply_text(random.choice(POEMS))


def main() -> None:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise SystemExit("Set the TELEGRAM_BOT_TOKEN environment variable first.")

    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        level=logging.INFO,
    )
    application = Application.builder().token(token).build()
    # Include commands too: the bot's promise is to answer every incoming message.
    application.add_handler(MessageHandler(filters.ALL, reply_with_poem))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
