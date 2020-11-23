from handlers import *
from mailru_im_async_bot.filter import Filter
from mailru_im_async_bot.bot import Bot
from mailru_im_async_bot.handler import MessageHandler, DefaultHandler, StartCommandHandler
from logging.config import fileConfig
from pid import PidFile
import logging
import configparser
import asyncio
import sys
import os

configs_path = os.path.realpath(os.path.dirname(sys.argv[0])) + "/"

# Get config path from args
if len(sys.argv) > 1:
	configs_path = sys.argv[1]

# Check exists config
if not os.path.isfile(os.path.join(configs_path, "logging.ini")):
	raise FileExistsError(f"File logging.ini not found in path {configs_path}")

logging.config.fileConfig(os.path.join(configs_path, "logging.ini"), disable_existing_loggers=False)
log = logging.getLogger(__name__)


NAME = "ball_of_fate2"
TOKEN = "***.**********.**********:*********"

loop = asyncio.get_event_loop()
bot = Bot(token=TOKEN, name=NAME)

# Register your handlers here
# ---------------------------------------------------------------------
bot.dispatcher.add_handler(StartCommandHandler(callback=start))
bot.dispatcher.add_handler(MessageHandler(
							callback=rand_color, 
							filters=Filter.regexp('(?i)цвет')
						)
					)
bot.dispatcher.add_handler(MessageHandler(
							callback=rand_number, 
							filters=Filter.regexp('(?i)(ск(о|а)льк(о|а)|как мн(о|а)г(о|а)|цифра|числ(о|а))')
						)
					)
bot.dispatcher.add_handler(MessageHandler(
							callback=media, 
							filters=Filter.media
						)
					)
bot.dispatcher.add_handler(MessageHandler(
							callback=media,
							filters=Filter.sticker
						)
					)
bot.dispatcher.add_handler(MessageHandler(
							callback=rand_prophecy, 
							filters=Filter.regexp('(?i)^("|«|»|“|)(предск(о|а)з(о|а)ние|п(о|а)г(о|а)дай|г(о|а)д(о|а)ние)')
						)
					)
bot.dispatcher.add_handler(DefaultHandler(
							callback=default_command
						)
					)


with PidFile(NAME):
	try:
		loop.create_task(bot.start_polling())
		loop.run_forever()
	finally:
		loop.close()
