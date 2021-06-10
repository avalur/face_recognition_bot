#!/usr/bin/env python

import io
import logging

import face_recognition

from telegram import Bot, ForceReply, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from PIL import Image

from config import token
"""
Simple Telegram Bot to make face recognition.

First, a few handler functions are defined. Then, those functions are 
passed to the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic example to make face recognition.
Press Ctrl-C on the command line or send a signal 
to the process to stop the bot.
"""

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers.
# These usually take the two arguments update and context.
def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\! ' +
        'Let me try to recognize faces on your foto\. Just upload it\.',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Usage: Basic example to make face recognition' +
                              'Just upload foto, pls.')


def text_message(update: Update, _: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(
        f"Thank you for sending: {update.message.text},\n" +
        f"but I am waiting only for images...")


def _make_rects(img_array, face_locations):
    img_res = img_array.copy()
    line_width = 3
    edge_color = [100, 100, 100]
    for location in face_locations:
        top, right, bottom, left = location
        img_res[top - line_width:top + line_width, left:right] = edge_color
        img_res[bottom - line_width:bottom + line_width, left:right] = edge_color
        img_res[top:bottom, left - line_width:left + line_width] = edge_color
        img_res[top:bottom, right - line_width:right + line_width] = edge_color
    return img_res


def make_face_recognition(update: Update, _: CallbackContext) -> None:
    # message.photo is a list of PhotoSize objects,
    # which represent different sizes of the same photo

    # print("Enter to make_face_recognition")
    img_from_user = update.message.photo[-1].get_file()
    img_file = io.BytesIO()
    img_from_user.download(out=img_file)
    img_array = face_recognition.load_image_file(img_file)
    # Find all the faces in the image
    face_locations = face_recognition.face_locations(img_array)
    # print(face_locations)
    img_with_rects = _make_rects(img_array, face_locations)
    out_file = 'tmp.jpg'
    Image.fromarray(img_with_rects, 'RGB').save(out_file, format="JPEG")
    update.message.bot.send_photo(
        update.message.chat_id,
        photo=open(out_file, 'rb'))


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    bot = Bot(token=token)
    updater = Updater(bot=bot, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands — answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message — echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, text_message))
    dispatcher.add_handler(MessageHandler(Filters.photo, make_face_recognition))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
